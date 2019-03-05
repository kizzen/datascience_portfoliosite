from flask import Flask, render_template, request # routes
from flask_mail import Mail, Message 

app = Flask(__name__)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT= 465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'karben1917@gmail.com',
	MAIL_PASSWORD = 'adversarial!'
	)

mail = Mail(app)

### FLASK ###

@app.route('/',methods=['POST', 'GET'])
def homepage():
	return render_template('index.html') 

if __name__ == '__main__':
	# app.run(host='0.0.0.0', port=80, debug=True)
	# app.run(host='https://thawing-ocean-73900.herokuapp.com/', port=80, debug=True)
	app.run()