from django import forms
from voucher_management.models import Voucher
from django.forms import ModelForm
from typing import Dict, Any

class VoucherRedemptionForm(ModelForm):
    """
    Form for redeeming a voucher.

    Attributes:
    - `code`: CharField - Field for entering the voucher code.

    Meta:
    - `model`: Voucher - The model associated with the form.
    - `fields`: List[str] - The list of fields to include in the form.

    Example:
    ```
    form = VoucherRedemptionForm(request.POST)
    if form.is_valid():
        # Process the form data
    ```
    """
    code = forms.CharField(
        label='Enter Voucher Code:',
        widget=forms.TextInput(
            attrs={
                'required': 'required',
            }
        )
    )  # type: forms.CharField

    class Meta:
        model = Voucher
        fields = ['code']  # type: List[str]
