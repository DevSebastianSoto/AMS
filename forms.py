from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, InputRequired


class ContactForm(FlaskForm):
    first_name = StringField(
        'Nombre',
        validators=[
            DataRequired()
        ]
    )
    last_name = StringField(
        'Apellido',
        validators=[
            DataRequired()
        ]
    )
    subject = StringField(
        'Asunto',
        validators=[
            DataRequired()
        ]
    )
    email = StringField(
        'Correo',
        validators=[
            DataRequired(), Email()
        ]
    )
    message = TextAreaField(
        'Su mensaje',
        validators=[
            DataRequired(),
            Length(max=500)
        ]
    )
