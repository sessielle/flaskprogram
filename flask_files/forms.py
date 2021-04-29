from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp


class RegistrationForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password",
                             validators=[DataRequired(), Length(min=12),
                                         Regexp("^(?=.*[a-z])", message="\nPassword must have a lowercase character"),
                                         Regexp("^(?=.*[A-Z])", message="\nPassword must have an uppercase character"),
                                         Regexp("^(?=.*\\d)", message="\nPassword must contain a number"),
                                         Regexp("(?=.*[@.$!%*#?&])", message="\nPassword must contain a special "
                                                                             "character")])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(),
                                                                           EqualTo("password"), Length(min=12)])
    submit = SubmitField(label="Sign Up")


class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password",
                             validators=[DataRequired(), Length(min=12),
                                         Regexp("^(?=.*[a-z])", message="\nPassword must have a lowercase character"),
                                         Regexp("^(?=.*[A-Z])", message="\nPassword must have an uppercase character"),
                                         Regexp("^(?=.*[0123456789])", message="\nPassword must contain a number"),
                                         Regexp("(?=.*[@.$!%*#?&])", message="\nPassword must contain a special "
                                                                             "character")])
    submit = SubmitField(label="Login")
