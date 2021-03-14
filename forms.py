from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
# from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=4,max=20)])
    password = PasswordField('Password',validators=[DataRequired(), Length(min=4,max=24)])
    submit = SubmitField(' Login ')

class test(FlaskForm):
    firstname = StringField('Firstname',validators=[DataRequired(), Length(min=4,max=24)])
    lastname = StringField('Lastname',validators=[DataRequired(), Length(min=4,max=24)])
    submit = SubmitField('Save to DB')