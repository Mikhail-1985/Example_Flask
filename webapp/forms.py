from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired # валидатор, сделает проверки

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})