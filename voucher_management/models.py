from django.db import models


class Voucher(models.Model):
    """
    Model representing a voucher.

    Attributes:
    - `SINGLE_REDEMPTION`: Constant for single redemption type.
    - `MULTIPLE_REDEMPTION`: Constant for multiple redemption type.
    - `X_TIMES_REDEMPTION`: Constant for X times redemption type.
    - `REDEMPTION_LIMIT_CHOICES`: Choices for the redemption type field.

    Fields:
    - `code` (CharField): Unique code for the voucher (max length: 20 characters).
    - `description` (TextField): Description of the voucher (nullable, blank allowed).
    - `discount_percentage` (PositiveIntegerField): Discount percentage for the voucher (default: 0).
    - `expiration_date` (DateTimeField): Expiration date of the voucher (nullable, blank allowed).
    - `redemption_type` (CharField): Type of redemption (single, multiple, or X times).
    - `redemption_limit` (PositiveIntegerField): Redemption limit for the voucher (nullable, blank allowed).
    - `redemption_count` (PositiveIntegerField): Current redemption count for the voucher (default: 0).
    - `is_active` (BooleanField): Indicates whether the voucher is active (default: True).
    """
    SINGLE_REDEMPTION = 'single'
    MULTIPLE_REDEMPTION = 'multiple'
    X_TIMES_REDEMPTION = 'x_times'

    REDEMPTION_LIMIT_CHOICES = [
        (SINGLE_REDEMPTION, 'Single Redemption'),
        (MULTIPLE_REDEMPTION, 'Multiple Redemption'),
        (X_TIMES_REDEMPTION, 'X times Redemption'),
    ]

    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=True, blank=True)
    discount_percentage = models.PositiveIntegerField(default=0)
    expiration_date = models.DateTimeField(null=True, blank=True)
    redemption_type = models.CharField(
        max_length=20,
        choices=REDEMPTION_LIMIT_CHOICES,
        default=SINGLE_REDEMPTION,
    )
    redemption_limit = models.PositiveIntegerField(null=True, blank=True)
    redemption_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
