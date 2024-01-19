from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.conf import settings


class DashboardView(LoginRequiredMixin, View):
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
