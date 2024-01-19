from django import forms
from django.forms import fields, widgets

from .models import Voucher


class UpdateVoucherForm(forms.Form):
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
