from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    file = FileField('Файл', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'], 'Только изображения')])
