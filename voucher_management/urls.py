from django.urls import path
from django.views.generic import RedirectView
from .views import VoucherManagementListView, VoucherManagementDetailView


urlpatterns = [
    path('', RedirectView.as_view(url='vouchers/', permanent=False)),
    path('vouchers/', VoucherManagementListView.as_view(), name='voucher_list'),
    path('vouchers/<int:pk>/', VoucherManagementDetailView.as_view(), name='voucher_detail'),
]
