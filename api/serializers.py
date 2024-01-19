from rest_framework import serializers
from .models import Voucher, VoucherApi


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'


class VoucherApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherApi
        fields = '__all__'
