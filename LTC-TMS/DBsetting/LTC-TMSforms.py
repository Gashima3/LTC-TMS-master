#
# User Management Forms
# author: Mason Hoffman, Nathan Yost
# created: 2/13/2018
# latest: 2/13/2018
# purpose: Team B's form classes for WTForms
#

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField, \
    BooleanField, FieldList, FormField, FileField, RadioField, SelectField, \
    TextAreaField, HiddenField
from wtforms.validators import InputRequired, EqualTo, Email, DataRequired


# Login form
class LoginForm(FlaskForm):
    email = StringField('Email', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
    loginButton = SubmitField('Login')
