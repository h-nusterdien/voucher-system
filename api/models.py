from django.db import models
from voucher_management.models import Voucher


class VoucherApi(models.Model):
    voucher = models.OneToOneField(Voucher, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.voucher.code
