from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_main.models import User

class RegisterationForm(FlaskForm):
    username=StringField('Username',
                        validators=[DataRequired(),Length(min=1,max=60)])
    email=StringField('Email',
                    validators=[DataRequired(),Email()])
    password=PasswordField('Password',
                        validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',
                        validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken')
    def validate_email(self,email):
        email=User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is already taken')

class LoginForm(FlaskForm):
    email=StringField('Email',
                    validators=[DataRequired(),Email()])
    password=PasswordField('Password',
                        validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login Up')
