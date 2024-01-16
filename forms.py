from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class MyForm(FlaskForm):
    file = FileField('Upload a file', validators=
    [
        FileRequired(),  # Ensure a file is selected
        FileAllowed(['pdf', 'pptx'], 'Only PDF, PPTX files are allowed')
    ])
    submit = SubmitField('Submit')