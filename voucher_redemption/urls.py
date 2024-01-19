from django.urls import path
from django.views.generic import RedirectView
from .views import VoucherRedemptionView


urlpatterns = [
    path('', RedirectView.as_view(url='redeem/', permanent=False)),
    path('redeem/', VoucherRedemptionView.as_view(), name='redeem_voucher'),
]