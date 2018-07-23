from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField, \
    BooleanField, FieldList, FormField, FileField, RadioField, SelectField, \
    TextAreaField, HiddenField
from wtforms.validator import InputRequired, EqualTo, Email, DataRequired


# Login form
 class LoginForm(FlaskForm):
     email = StringField('Email', [InputRequired()])
     password = PasswordField('Password', [InputRequired()])
     loginButton = SubmitField('Login')

class Patient(FlaskForm):
    fname=StringField("First Name", [InputReqired()])
    lname=StringField("Last Name", [InputRequired()])
    gender=RadioField("Gender", choices = [("male","Male"),("female","Female")])
    birthday=DateField("Birthday", format="%Y-%m-%d")
    
