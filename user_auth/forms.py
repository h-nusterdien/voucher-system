from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    Form for user login.

    Fields:
    - `username` (CharField): Field for entering the username.
    - `password` (CharField): Field for entering the password (masked).
    """

    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    """
    Form for user sign-up.

    Fields:
    - `username` (CharField): Field for entering the username.
    - `email` (EmailField): Field for entering the email.
    - `password1` (CharField): Field for entering the password (masked).
    - `password2` (CharField): Field for confirming the password (masked).
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
