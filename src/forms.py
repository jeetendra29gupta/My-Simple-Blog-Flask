from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length

from src.models import BlogStatus


class SignupForm(FlaskForm):
    fullname = StringField(
        "Full Name", validators=[DataRequired(), Length(min=3, max=120)]
    )
    email_id = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])

    submit = SubmitField("Create Account")


class SigninForm(FlaskForm):
    email_id = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Sign In")


class BlogForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=300)])
    body = TextAreaField("Body", validators=[DataRequired()])
    status = SelectField(
        "Status",
        # choices=[("draft", "Draft"), ("published", "Published")],
        choices=[(status.value, status.name.upper()) for status in BlogStatus],
        default="draft",
        validators=[DataRequired()],
    )
    submit = SubmitField("Create Blog")
