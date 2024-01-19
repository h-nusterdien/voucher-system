from django.db import models
from django.contrib.auth.models import User
from voucher_management.models import Voucher


class VoucherRedemption(models.Model):
    """
    Model representing the redemption of a voucher by a user.

    Fields:
    - `user`: ForeignKey to User - The user who redeemed the voucher.
    - `voucher`: ForeignKey to Voucher - The voucher that was redeemed.
    - `redeemed_at`: DateTimeField - The timestamp when the voucher was redeemed.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)
