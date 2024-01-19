from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.conf import settings
from .forms import LoginForm, SignUpForm


class UserAuth(View):
    """
    Base view for user authentication-related functionality.

    Attributes:
    - `base_context` (dict): Base context with URLs for signup, login, and logout.
    """

    base_context = {
        'urls': {
            'signup': settings.SIGN_UP_URL,
            'login': settings.LOGIN_URL,
            'logout': settings.LOGOUT_URL,
        }
    }


class LoginView(UserAuth):
    """
    View for handling user login.

    Attributes:
    - `template` (str): Template for rendering the login page.
    - `form` (LoginForm): Form for user login.
    """

    template = 'user_auth/login.html'
    form = LoginForm()

    def get(self, request):
        """
        Handle GET request for rendering the login page.

        Returns:
        - Rendered HTML page for user login.
        """
        context = {
            'form': self.form,
        }
        context.update(self.base_context)
        return render(request, self.template, context)
    
    def post(self, request):
        """
        Handle POST request for user login.

        Parameters:
        - `request` (HttpRequest): HTTP request object.

        Returns:
        - Redirects to the appropriate page after login.
        """
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect('voucher_list')
            return redirect('redeem_voucher')
        else:
            form = LoginForm(request.POST)
            context = {
                'form': form,
                'error': 'Please enter a correct username and password.'
            }

        context.update(self.base_context)
        return render(request, self.template, context)


class LogoutView(UserAuth):
    """
    View for handling user logout.

    Attributes:
    - `template` (str): Template for rendering the logout page.
    - `form` (None): No form needed for logout.
    """

    template = None

    def get(self, request):
        """
        Handle GET request for user logout.

        Parameters:
        - `request` (HttpRequest): HTTP request object.

        Returns:
        - Redirects to the login page after logout.
        """
        if request.user.is_authenticated:
            logout(request)
        return redirect(settings.LOGIN_URL)


class SignupView(UserAuth):
    """
    View for handling user signup.

    Attributes:
    - `template` (str): Template for rendering the signup page.
    - `form` (SignUpForm): Form for user signup.
    """

    template = 'user_auth/signup.html'
    form = SignUpForm()

    def get(self, request):
        """
        Handle GET request for rendering the signup page.

        Returns:
        - Rendered HTML page for user signup.
        """
        context = {
            'form': self.form,
        }
        context.update(self.base_context)
        return render(request, self.template, context)
    
    def post(self, request):
        """
        Handle POST request for user signup.

        Parameters:
        - `request` (HttpRequest): HTTP request object.

        Returns:
        - Redirects to the login page after successful signup.
        """
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
        context = {
            'form': form,
        }
        context.update(self.base_context)
        return render(request, self.template, context)
