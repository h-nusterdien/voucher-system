from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.conf import settings
from .forms import LoginForm, SignUpForm
from django.http import HttpRequest, HttpResponse
from typing import Dict, Any


class UserAuth(View):
    """
    Base class for user authentication views.

    Attributes:
    - `base_context`: Dict[str, Any] - Base context containing URLs for signup, login, and logout.
    """

    base_context: Dict[str, Any] = {
        'urls': {
            'signup': settings.SIGN_UP_URL,
            'login': settings.LOGIN_URL,
            'logout': settings.LOGOUT_URL,
        }
    }


class LoginView(UserAuth):
    """
    View class for user login.

    Attributes:
    - `template`: str - Template name for rendering the login page.
    - `form`: LoginForm - Form instance for user login.
    """

    template: str = 'user_auth/login.html'
    form: LoginForm = LoginForm()

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handle GET requests for the login view.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - HttpResponse: The HTTP response.
        """
        context: Dict[str, Any] = {
            'form': self.form,
        }
        context.update(self.base_context)
        return render(request, self.template, context)
    
    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Handle POST requests for the login view.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - HttpResponse: The HTTP response.
        """
        username: str = request.POST["username"]
        password: str = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect('voucher_list')
            return redirect('redeem_voucher')
        else:
            form: LoginForm = LoginForm(request.POST)
            context: Dict[str, Any] = {
                'form': form,
                'error': 'Please enter a correct username and password.'
            }

        context.update(self.base_context)
        return render(request, self.template, context)


class LogoutView(UserAuth):
    """
    View class for user logout.

    Methods:
    - `get`: Handle GET requests for user logout.

    Attributes:
    - `template`: str - Template name for rendering the logout page.
    """

    template: str = 'user_auth/logout.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handle GET requests for the logout view.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - HttpResponse: The HTTP response.
        """
        if request.user.is_authenticated:
            logout(request)
        return redirect(settings.LOGIN_URL)


class SignupView(UserAuth):
    """
    View class for user signup.

    Attributes:
    - `template`: str - Template name for rendering the signup page.
    - `form`: SignUpForm - Form instance for user signup.
    """

    template: str = 'user_auth/signup.html'
    form: SignUpForm = SignUpForm()

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handle GET requests for the signup view.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - HttpResponse: The HTTP response.
        """
        context: Dict[str, Any] = {
            'form': self.form,
        }
        context.update(self.base_context)
        return render(request, self.template, context)
    
    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Handle POST requests for the signup view.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - HttpResponse: The HTTP response.
        """
        form: SignUpForm = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
        context: Dict[str, Any] = {
            'form': form,
        }
        context.update(self.base_context)
        return render(request, self.template, context)
