from django.db import models
from django.contrib.auth.models import User


class Voucher(models.Model):
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
