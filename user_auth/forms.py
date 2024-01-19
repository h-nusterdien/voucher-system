from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    Form for user login.

    Fields:
    - username: CharField for username input.
    - password: CharField for password input (masked).
    """
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    """
    Form for user sign-up.

    Fields:
    - username: CharField for username input.
    - email: EmailField for user email input.
    - password1: CharField for password input (masked).
    - password2: CharField to confirm the password (masked).
    """
    email = forms.EmailField(label="Email")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
