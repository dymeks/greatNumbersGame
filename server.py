from flask import Flask, render_template, request, redirect,session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def landing_page():
	random_number = random.randint(0,100)
	if not ('number' in session):
		session['number'] = random_number
	print str(session['number']) 	

	return render_template('index.html',response_class ='hide',play_again='hide',guess ='show')

@app.route('/guess',methods=['POST'])

def guess():
	response_class ='red'
	response = ''
	guess_class = 'show'
	play_again = 'hide'
	
	if int(request.form['guess']) == session['number']:
		response_class = 'green'
		response = str(session['number']) + 'was the number!'
		guess_class = 'hide'
		play_again = 'show'
	elif int(request.form['guess']) > session['number']:	
		response = "Too High!"
		
	elif int(request.form['guess']) < session['number']:
		response = "Too Low!"
	print str(session['number'])	
	return render_template('index.html',response_class=response_class,response=response,play_again=play_again,guess=guess_class)
@app.route('/reset',methods=['POST'])
def reset_game():
	random_number = random.randint(0,100)
	session['number'] = random_number
	return redirect('/')
app.run(debug=True)				

