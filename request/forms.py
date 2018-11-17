from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, SelectField, DateField
from .models import ProductEnum
from wtforms.validators import DataRequired

class RequestForm(FlaskForm):
    client = IntegerField('Client')
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    priority = IntegerField('Priority')
    target_date = DateField('Target Date')
    product = SelectField('Product', choices=[(x.name, x.name) for x in ProductEnum])
