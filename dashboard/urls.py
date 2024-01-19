from django.urls import path, include
from .views import DashboardView


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('voucher-management/', include('voucher_management.urls')),
    path('voucher-redemption/', include('voucher_redemption.urls')),
]