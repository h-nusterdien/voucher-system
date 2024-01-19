from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.conf import settings
from typing import Dict, Any


class DashboardView(LoginRequiredMixin, View):
    """
    Base class for dashboard views.

    Attributes:
    - `login_url`: str - The URL to redirect to for login.
    - `dashboard_context`: Dict[str, Any] - The context for the dashboard view.

    Example:
    ```
    class MyDashboardView(DashboardView):
        template_name = 'my_dashboard.html'
        dashboard_context = {
            'header': {
                'title': 'My Dashboard',
            }
        }
    ```
    """

    login_url: str = settings.LOGIN_URL  # type: str

    dashboard_context: Dict[str, Any] = {
        'header': {
            'urls': {
                'sign_up': settings.SIGN_UP_URL,
                'login': settings.LOGIN_URL,
                'logout': settings.LOGOUT_URL,
            }
        },
    }  # type: Dict[str, Any]
