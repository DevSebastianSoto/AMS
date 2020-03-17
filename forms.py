from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, InputRequired

class ContactForm(FlaskForm):
    first_name = StringField(
        'First name',
        validators=[
            DataRequired()         
        ]
    )
    last_name = StringField(
        'Last name',
        validators=[
            DataRequired()            
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(), Email()        
        ]
    )
    message = TextAreaField(
        'Your Message',
        validators=[
            DataRequired(),
            Length(max=500)
        ]
    )
    
