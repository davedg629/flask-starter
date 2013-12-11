from flask_wtf import Form
from wtforms import TextField, DateField, \
    PasswordField, IntegerField, SelectField
from wtforms.validators import Required, Length


class SampleForm(Form):
    title = TextField('Title', validators=[Required()])
    posted_date = DateField('Posted Date (yyyy/mm/dd)',
                            validators=[Required()], format='%Y/%m/%d')
    select_field = SelectField('Priority', validators=[Required()],
                               choices=[('1', '1'), ('2', '2'), ('3', '3'),
                                        ('4', '4'), ('5', '5')])
    rating_integer = IntegerField('Rating',
                                  validators=[Required()])
    post_body = TextField('Post',
                          validators=[Required(), Length(min=1, max=1000)])


class LoginForm(Form):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
