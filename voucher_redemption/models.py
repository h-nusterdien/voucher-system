from django.db import models
from django.contrib.auth.models import User
from voucher_management.models import Voucher


class VoucherRedemption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)
