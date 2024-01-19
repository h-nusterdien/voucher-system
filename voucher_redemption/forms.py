from django import forms
from voucher_management.models import Voucher


class VoucherRedemptionForm(forms.ModelForm):
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