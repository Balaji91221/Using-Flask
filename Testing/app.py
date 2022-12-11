import pyrebase
from flask import Flask, render_template, request

app = Flask(__name__)
config = {
  "apiKey": "AIzaSyBePDWCVjlTuh1GgMZhmC1V57YAVLJzbRs",
  "authDomain": "using-flask-ffac6.firebaseapp.com",
  "databaseURL": "https://using-flask-ffac6-default-rtdb.firebaseio.com",
  "projectId": "using-flask-ffac6",
  "storageBucket": "using-flask-ffac6.appspot.com",
  "messagingSenderId": "477046720843",
  "appId": "1:477046720843:web:da078b09f9864853d000ce",
  "measurementId": "G-RVZ4B865TM"
}

firebase = pyrebase.initialize_app(config) 
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])

def basic():
	unsuccessful = 'Please check your credentials'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_up_with_email_and_password(email, password)
			return render_template('new.html', s=successful)
		except:
			return render_template('new.html', us=unsuccessful)

	return render_template('new.html')


if __name__ == '__main__':
	app.run(debug=True)
