from django import forms
from voucher_management.models import Voucher


class VoucherRedemptionForm(forms.ModelForm):
    """
    Form for redeeming a voucher.

    Fields:
    - `code`: CharField - Input for the voucher code.

    Attributes:
    - `required`: Indicates that the voucher code is a required field.
    """
    class Meta:
        model = Voucher
        fields = ['code']

    code = forms.CharField(
        label='Enter Voucher Code:',
        widget=forms.TextInput(
            attrs={
                'required': 'required',
            }
        )
    )
