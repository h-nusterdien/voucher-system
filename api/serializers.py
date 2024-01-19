from rest_framework import serializers
from .models import Voucher, VoucherApi


class VoucherSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Voucher model.

    Meta:
    - `model` (Model): Voucher model.
    - `fields` (list): List of fields to include in the serialization (all fields in this case).
    """
    class Meta:
        model = Voucher
        fields = '__all__'


class VoucherApiSerializer(serializers.ModelSerializer):
    """
    Serializer class for the VoucherApi model.

    Meta:
    - `model` (Model): VoucherApi model.
    - `fields` (list): List of fields to include in the serialization (all fields in this case).
    """
    class Meta:
        model = VoucherApi
        fields = '__all__'
