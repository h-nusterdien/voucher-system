from django import forms
from django.forms import fields, widgets

from .models import Voucher


class UpdateVoucherForm(forms.Form):
    """
    Form for updating voucher details.

    Fields:
    - `code` (CharField): Voucher code (optional).
    - `description` (CharField): Voucher description (optional).
    - `discount_percentage` (IntegerField): Discount percentage (optional).
    - `redemption_type` (ChoiceField): Redemption type (optional).
    - `x_times_redemption_limit` (IntegerField): X times redemption limit (optional).
    - `expiration_date` (DateTimeField): Expiration date (optional, with date picker widget).
    - `is_active` (BooleanField): Active status (optional, default: True).
    """
    code = fields.CharField(
        required=False,
    )
    description = fields.CharField(
        required=False,
    )
    discount_percentage = fields.IntegerField(
        required=False,
        label="Discount Percentage",
    )
    redemption_type = fields.ChoiceField(
        required=False,
        label="Redemption Type",
        choices=Voucher.REDEMPTION_LIMIT_CHOICES,
    )
    x_times_redemption_limit = fields.IntegerField(
        required=False,
        label="X Times Redemption Limit",
    )
    expiration_date = fields.DateTimeField(
        required=False,
        label="Expiration Date",
        widget=widgets.TextInput(attrs={'type': 'date'})
    )
    is_active = fields.BooleanField(
        required=False,
        initial=True,
    )


class CreateVoucherForm(forms.Form):
    """
    Form for creating a new voucher.

    Fields:
    - `code` (CharField): Voucher code.
    - `description` (CharField): Voucher description (optional).
    - `discount_percentage` (IntegerField): Discount percentage.
    - `redemption_type` (ChoiceField): Redemption type.
    - `x_times_redemption_limit` (IntegerField): X times redemption limit (optional).
    - `expiration_date` (DateTimeField): Expiration date (optional, with date picker widget).
    """
    code = fields.CharField()
    description = fields.CharField(
        required=False,
    )
    discount_percentage = fields.IntegerField(
        label="Discount Percentage",
    )
    redemption_type = fields.ChoiceField(
        label="Redemption Type",
        choices=Voucher.REDEMPTION_LIMIT_CHOICES,
    )
    x_times_redemption_limit = fields.IntegerField(
        label="X Times Redemption Limit",
        required=False,
    )
    expiration_date = fields.DateTimeField(
        label="Expiration Date",
        required=False,
        widget=widgets.TextInput(attrs={'type': 'date'})
    )
