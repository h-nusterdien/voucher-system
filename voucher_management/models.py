from django.db import models
from typing import Tuple, Optional, List


class Voucher(models.Model):
    """
    Model representing a voucher with various features.

    Attributes:
    - `SINGLE_REDEMPTION`: str - Constant for single redemption type.
    - `MULTIPLE_REDEMPTION`: str - Constant for multiple redemption type.
    - `X_TIMES_REDEMPTION`: str - Constant for X times redemption type.
    - `REDEMPTION_LIMIT_CHOICES`: List[Tuple[str, str]] - Choices for redemption types.
    - `code`: str - Voucher code (max length 20 characters, unique).
    - `description`: Optional[str] - Voucher description (nullable).
    - `discount_percentage`: int - Discount percentage for the voucher (default 0).
    - `expiration_date`: Optional[str] - Expiration date for the voucher (nullable).
    - `redemption_type`: str - Redemption type for the voucher (choices: single, multiple, x_times; default: single).
    - `redemption_limit`: Optional[int] - Redemption limit for the voucher (nullable).
    - `redemption_count`: int - Current redemption count for the voucher (default 0).
    - `is_active`: bool - Flag indicating if the voucher is active (default True).
    """
    SINGLE_REDEMPTION: str = 'single'
    MULTIPLE_REDEMPTION: str = 'multiple'
    X_TIMES_REDEMPTION: str = 'x_times'

    REDEMPTION_LIMIT_CHOICES: List[Tuple[str, str]] = [
        (SINGLE_REDEMPTION, 'Single Redemption'),
        (MULTIPLE_REDEMPTION, 'Multiple Redemption'),
        (X_TIMES_REDEMPTION, 'X times Redemption'),
    ]

    code: str = models.CharField(max_length=20, unique=True)
    description: Optional[str] = models.TextField(null=True, blank=True)
    discount_percentage: int = models.PositiveIntegerField(default=0)
    expiration_date: Optional[str] = models.DateTimeField(null=True, blank=True)
    redemption_type: str = models.CharField(max_length=20, choices=REDEMPTION_LIMIT_CHOICES, default=SINGLE_REDEMPTION)
    redemption_limit: Optional[int] = models.PositiveIntegerField(null=True, blank=True)
    redemption_count: int = models.PositiveIntegerField(default=0)
    is_active: bool = models.BooleanField(default=True)
