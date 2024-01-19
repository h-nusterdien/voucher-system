from django.urls import path
from django.views.generic import RedirectView
from .views import LoginView, LogoutView, SignupView

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=False)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]