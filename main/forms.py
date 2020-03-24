from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, InputRequired


class ContactForm(FlaskForm):
    first_name = StringField(
        'Nombre',
        validators=[DataRequired(), Length(min=2, max=20)]
    )
    last_name = StringField(
        'Apellido',
        validators=[DataRequired(), Length(min=2, max=20)]
    )
    subject = StringField(
        'Asunto',
        validators=[DataRequired(), Length(min=2, max=30)]
    )
    email = StringField(
        'Correo',
        validators=[DataRequired(), Email()]
    )
    message = TextAreaField(
        'Su mensaje',
        validators=[DataRequired(), Length(max=500)]
    )
