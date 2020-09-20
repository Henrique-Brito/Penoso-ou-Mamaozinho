from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask import redirect, url_for,  flash, jsonify
from functools import wraps
import re, unidecode

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


def success_response(data=None):
	status = {
		'status': 'success'
	}
	if data:
		data.update(status)
	else: 
		data = status

	return jsonify(data)


def error_response(message=''):
	return jsonify({
		'status': 'error',
		'message': message
	})


def sanitizeString(string):
    string = re.sub('ª', ' ', string)
    string = re.sub('º', ' ', string)
    string = re.sub('°', ' ', string)

    # remove all accents 
    string = unidecode.unidecode(string)

    # Remove all Markup tags in string
    p = re.compile(r'<.*?>')
    string = p.sub('', string)

    string = re.sub(r'[^A-Za-z0-9]+', '', string)
    
    return string.lower()