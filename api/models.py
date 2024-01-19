from django.db import models
from voucher_management.models import Voucher


class VoucherApi(models.Model):
    """
    Model class representing the association between Voucher and additional API-related information.

    Fields:
    - `voucher` (OneToOneField): One-to-one relationship with the Voucher model.
    - `description` (TextField): Additional description for the associated voucher.

    Methods:
    - `__str__`: Returns the string representation of the model instance based on the associated voucher's code.
    """
    voucher = models.OneToOneField(Voucher, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        """
        Returns the string representation of the VoucherApi instance based on the associated voucher's code.

        Returns:
        - str: String representation of the VoucherApi instance.
        """
        return self.voucher.code
