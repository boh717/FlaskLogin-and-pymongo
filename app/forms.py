from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    """Login form to access writing and settings pages"""

    username = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
