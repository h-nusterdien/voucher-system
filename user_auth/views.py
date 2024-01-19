from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.conf import settings
from .forms import LoginForm, SignUpForm


class UserAuth(View):
    base_context = {
        'urls': {
            'signup': settings.SIGN_UP_URL,
            'login': settings.LOGIN_URL,
            'logout': settings.LOGOUT_URL,
        }
    }


class LoginView(UserAuth):
    template = 'user_auth/login.html'
    form = LoginForm()

    def get(self, request):
        context = {
            'form': self.form,
        }
        context.update(self.base_context)
        return render(request, self.template, context)
    
    def post(self, request):
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
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect(settings.LOGIN_URL)


class SignupView(UserAuth):
    template = 'user_auth/signup.html'
    form = SignUpForm()

    def get(self, request):
        context = {
            'form': self.form,
        }
        context.update(self.base_context)
        return render(request, self.template, context)
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
        context = {
            'form': form,
        }
        context.update(self.base_context)
        return render(request, self.template, context)
