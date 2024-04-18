from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, StringField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(message="Поле не должно быть пустым")])
    description = TextAreaField('Описание', validators=[DataRequired(message="Поле не должно быть пустым")])
    image = FileField()
    submit = SubmitField('Добавить фильм')

class ReviewForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(message="Поле не должно быть пустым")])
    text = TextAreaField('Текст отзыва', validators=[DataRequired(message="Поле не должно быть пустым")])
    score = SelectField('Оценка', choices=[(i, i) for i in range(1,11)])
    submit = SubmitField('Добавить отзыв')