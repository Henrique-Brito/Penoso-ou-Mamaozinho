from __future__ import print_function
import sys
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

import logging
app = Flask(__name__)

# configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '****'
app.config['MYSQL_DB'] = 'teste'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# initialize MySQL
mysql = MySQL(app)


# Home page
@app.route('/')
def index():
	#create cursor
	return redirect(url_for('login'))

@app.route('/about')
def about():
	return render_template('about.html')


# Disable dashboard if user is logged in:
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Please login to view dashboard', 'danger')
			return redirect(url_for('login'))
	return wrap


@app.route('/disciplinas')
# @is_logged_in
def disciplinas():
	#create cursor
	cur = mysql.connection.cursor()

	result = cur.execute("SELECT * FROM disciplinas")

	disciplinas = cur.fetchall()

	if result > 0:
		return render_template('disciplinas.html',disciplinas=disciplinas)
	else:
		msg = "No disciplinas Found"
		return render_template('disciplinas.html',msg=msg)

	cur.close()



# User registration class
class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='passwords do not match')
		])
	confirm = PasswordField('confirm password')


# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))

		# create a cursor to mysqldb
		cur = mysql.connection.cursor()

		cur.execute("INSERT INTO users(name, email, username, password) VALUES (%s, %s, %s, %s)", (name, email, username, password))

		# commit changes to db
		mysql.connection.commit()

		# close connection to db
		cur.close()
		flash('Registration completed successfully', 'success')

		return redirect(url_for('login'))

	return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET' and 'logged_in' in session:
		return redirect(url_for("disciplinas"))

	if request.method == 'POST':
		# get form data
		username = request.form['username']
		passwordEntered = request.form['password']

		# create mysql cursor
		cur = mysql.connection.cursor()

		# get user by username
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

		if result > 0:
			# get stored hash
			data = cur.fetchone()
			correctPassword = data['password']

			# compare hash with entered hash
			if sha256_crypt.verify(passwordEntered, correctPassword):
				session['logged_in'] = True
				session['username'] = username
				session['id'] = data["id"]

				flash('You are now logged in', 'success')
				# return redirect(url_for('dashboard'))
				return redirect(url_for("disciplinas"))
			else:
				error = 'Invalid login'
				return render_template('login.html', error=error)
			cur.close()
		else:
			error = 'Username not found'
			return render_template('login.html', error=error)

	return render_template('login.html')


# log out
@app.route('/logout')
@is_logged_in
def logout():
	session.clear()
	flash('Successfully logged out', 'success')
	return redirect(url_for('login'))






if __name__ == '__main__':
	app.secret_key = 'secret123'
	app.run(debug=True)


# ALTER TABLE disciplinas  add mamao  INT UNSIGNED
# ALTER TABLE disciplinas  add penoso  INT UNSIGNED
