from django.db import models
from django.contrib.auth.models import User
from voucher_management.models import Voucher


class VoucherRedemption(models.Model):
    """
    Model representing the redemption of a voucher by a user.

    Fields:
    - `user`: ForeignKey - Reference to the User who redeemed the voucher.
    - `voucher`: ForeignKey - Reference to the Voucher being redeemed.
    - `redeemed_at`: DateTimeField - Timestamp indicating when the redemption occurred.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)
