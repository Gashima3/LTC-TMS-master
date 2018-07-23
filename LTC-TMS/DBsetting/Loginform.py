from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField, \
    BooleanField, FieldList, FormField, FileField, RadioField, SelectField, \
    TextAreaField, HiddenField
from wtforms.validators import InputRequired, EqualTo, Email, DataRequired


# Login form
class LoginForm(FlaskForm):
    Staff_ID = StringField('staff_ID', [InputRequired()])
    password = PasswordField("password", [InputRequired()])
    loginButton = SubmitField('Login')
