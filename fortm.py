from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class ApplicationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    course = SelectField('Курс', choices=[
        ('programming', 'Программирование'),
        ('design', 'Дизайн'),
        ('languages', 'Иностранные языки'),
        ('finance', 'Финансовая грамотность')
    ], validators=[DataRequired()])
    submit = SubmitField('Отправить заявку')