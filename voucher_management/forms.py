from django import forms
from django.forms import fields, widgets
from typing import Optional, Tuple
from .models import Voucher


class UpdateVoucherForm(forms.Form):
    """
    Form for updating voucher information.

    Attributes:
    - `code`: Optional[str] - Voucher code.
    - `description`: Optional[str] - Voucher description.
    - `discount_percentage`: Optional[int] - Discount percentage for the voucher.
    - `redemption_type`: Optional[str] - Redemption type for the voucher.
    - `x_times_redemption_limit`: Optional[int] - X times redemption limit for the voucher.
    - `expiration_date`: Optional[str] - Expiration date for the voucher (formatted as 'YYYY-MM-DD').
    - `is_active`: Optional[bool] - Flag indicating if the voucher is active.
    """
    code: Optional[str] = fields.CharField(required=False)
    description: Optional[str] = fields.CharField(required=False)
    discount_percentage: Optional[int] = fields.IntegerField(required=False, label="Discount Percentage")
    redemption_type: Optional[str] = fields.ChoiceField(required=False, label="Redemption Type", choices=Voucher.REDEMPTION_LIMIT_CHOICES)
    x_times_redemption_limit: Optional[int] = fields.IntegerField(required=False, label="X Times Redemption Limit")
    expiration_date: Optional[str] = fields.DateTimeField(required=False, label="Expiration Date", widget=widgets.TextInput(attrs={'type': 'date'}))
    is_active: Optional[bool] = fields.BooleanField(required=False, initial=True)


class CreateVoucherForm(forms.Form):
    """
    Form for creating a new voucher.

    Attributes:
    - `code`: str - Voucher code.
    - `description`: Optional[str] - Voucher description.
    - `discount_percentage`: int - Discount percentage for the voucher.
    - `redemption_type`: str - Redemption type for the voucher.
    - `x_times_redemption_limit`: Optional[int] - X times redemption limit for the voucher.
    - `expiration_date`: Optional[str] - Expiration date for the voucher (formatted as 'YYYY-MM-DD').
    """
    code: str = fields.CharField()
    description: Optional[str] = fields.CharField(required=False)
    discount_percentage: int = fields.IntegerField(label="Discount Percentage")
    redemption_type: str = fields.ChoiceField(label="Redemption Type", choices=Voucher.REDEMPTION_LIMIT_CHOICES)
    x_times_redemption_limit: Optional[int] = fields.IntegerField(required=False, label="X Times Redemption Limit")
    expiration_date: Optional[str] = fields.DateTimeField(required=False, label="Expiration Date", widget=widgets.TextInput(attrs={'type': 'date'}))
