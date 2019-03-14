from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, PasswordField
from wtforms.validators import DataRequired, Regexp
import datetime

from models import Entry

date_format_error_msg = ("Must use mm/dd/YYY format!")

def invalid_date(form, field):
    try:
        datetime.datetime.strptime(field.data, '%m/%d/%Y')
    except ValueError:
        raise ValidationError('The date you entered is invalid. Try Again.')


class EntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    date = DateTimeField('Date', 
                          validators=[DataRequired(),
                                      Regexp(r'\d{2}\/\d{2}\/\d{4}',
                                      message=date_format_error_msg),
                                      invalid_date])

    time_spent = StringField('Time Spent', validators=[DataRequired()])

    entry_text = TextAreaField('Entry', validators=[DataRequired()])

    resources_text = StringField('Resources to Remeber',
                                  validators=[DataRequired()])
