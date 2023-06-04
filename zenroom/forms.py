from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.widgets import TextArea


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=3, max=200)])
    password = StringField('Password',
                           validators=[DataRequired(), Length(min=3, max=2000)])
    submit = SubmitField('Submit')
    

class Diary(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=200)])
    note = StringField('Note',
                           validators=[DataRequired(), Length(min=3, max=2000)], widget=TextArea())
    submit = SubmitField('Submit')

class Diet(FlaskForm):
    age = IntegerField("Age",validators=[DataRequired(), Length(max=4)])
    gender=SelectField("Gender",choices=[('male','Male'),('female','Female'),('other','Other')])
    diseases=StringField("Diseases",validators=[Length(min=3,max=200)])
    calories=IntegerField("Calories",validators=[Length(max=4)])
    submit = SubmitField('Submit')