from flask.ext.wtf import Form
    from wtforms import StringField, BooleanField
    from wtforms.validators import DataRequired

    Class FirePut(Form):
        title = StringField(‘title’, validators=[DataRequired()])
        year = StringField(‘year’, validators=[DataRequired()])
        rating = StringField(‘rating’, validators=[DataRequired()])
