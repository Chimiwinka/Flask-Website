# Need this for all our forms
from random import choices
from flask_wtf import FlaskForm

# Fields
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    EmailField,
    SelectField,
    HiddenField,
)

# Validators
from wtforms.validators import (
    DataRequired,
    EqualTo,
    ValidationError,
    Regexp,
    InputRequired,
)
from blog.models import User

"""
Form with:
- First name (string)
- Submit button (submit)
"""


class RegistrationForm(FlaskForm):
    username = StringField(
        "First Name",
        validators=[
            DataRequired(),
            Regexp(
                "^[a-z]{6,20}$",
                message="Your username should be between 6 and 20 characters long, and can only contain lowercase letters and numbers.",
            ),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords do not match. Try again"),
        ],
    )
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(
                "Username already exist. Please choose a different one."
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email already exist. Please choose a different one.")


class LoginForm(FlaskForm):
    username = EmailField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class AddCommentForm(FlaskForm):
    comment = StringField(
        "You can leave a comment here ! ", validators=[InputRequired()]
    )
    submit = SubmitField("Post")


class SortingForm(FlaskForm):
    sort_post = SelectField(
        "Order by date",
        choices=[("date_asc", "Ascending"), ("date_desc", "Descending")],
    )
    submit = SubmitField()


class RatingForm(FlaskForm):
    rating = HiddenField("Enter Rating", validators=[InputRequired()])
