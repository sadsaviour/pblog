from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class LoginForm(FlaskForm):
	openid = StringField('openid',[validators.required()])
	remember_me = BooleanField('remember_me',default = False)
