from django.urls import path, include
from .views import VoucherAPIListView, VoucherAPIDetailView


urlpatterns = [
    path('vouchers/', VoucherAPIListView.as_view(), name='api_voucher_list'),
    path('vouchers/<int:pk>/', VoucherAPIDetailView.as_view(), name='api_voucher_detail'),
]
