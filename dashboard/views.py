from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.conf import settings


class DashboardView(LoginRequiredMixin, View):
    """
    A view for the dashboard that requires the user to be logged in.

    Attributes:
    - `login_url` (str): URL to redirect to for login.
    - `dashboard_context` (dict): Context data for the dashboard view, including header URLs.
    """
    login_url = settings.LOGIN_URL

    dashboard_context = {
        'header': {
            'urls': {
                'sign_up': settings.SIGN_UP_URL,
                'login': settings.LOGIN_URL,
                'logout': settings.LOGOUT_URL,
            }
        },
    }
