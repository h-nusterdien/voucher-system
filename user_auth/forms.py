from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from typing import Dict, Any

class LoginForm(forms.Form):
    """
    Form for user login.

    Fields:
    - `username`: CharField for username input.
    - `password`: CharField for password input (masked).
    """

    username: forms.CharField = forms.CharField(label="Username")  # type: forms.CharField
    password: forms.CharField = forms.CharField(label="Password", widget=forms.PasswordInput)  # type: forms.CharField


class SignUpForm(UserCreationForm):
    """
    Form for user sign-up.

    Fields:
    - `username`: CharField for username input.
    - `email`: EmailField for user email input.
    - `password1`: CharField for password input (masked).
    - `password2`: CharField to confirm the password (masked).
    """

    email: forms.EmailField = forms.EmailField(label="Email")  # type: forms.EmailField

    class Meta:
        model: User = User  # type: Any
        fields: list = ['username', 'email', 'password1', 'password2']  # type: List[str]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the SignUpForm.

        Parameters:
        - `args`: Any - Variable-length argument list.
        - `kwargs`: Any - Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
