from django.db import models
from voucher_management.models import Voucher
from typing import Any


class VoucherApi(models.Model):
    """
    Model representing a VoucherApi instance.

    Attributes:
    - `voucher`: Voucher - The associated Voucher instance.
    - `description`: str - The description for the VoucherApi instance.
    """

    voucher: models.OneToOneField[Voucher, Any] = models.OneToOneField(Voucher, on_delete=models.CASCADE)  # type: models.OneToOneField[Voucher, Any]
    description: models.TextField = models.TextField()  # type: models.TextField

    def __str__(self) -> str:
        """
        Return a string representation of the VoucherApi instance.

        Returns:
        - str: The voucher code as the string representation.
        """
        return str(self.voucher.code)
