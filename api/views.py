from rest_framework import generics
from .models import Voucher, VoucherApi
from .serializers import VoucherSerializer, VoucherApiSerializer
from typing import Any, List


class VoucherAPIListView(generics.ListCreateAPIView):
    """
    API view for listing and creating Voucher instances.

    Attributes:
    - `queryset`: Queryset - The queryset of Voucher instances.
    - `serializer_class`: VoucherSerializer - The serializer class for Voucher instances.
    """

    queryset: Any = Voucher.objects.all()  # type: Any
    serializer_class: VoucherSerializer = VoucherSerializer  # type: VoucherSerializer


class VoucherAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific Voucher instance.

    Attributes:
    - `queryset`: Queryset - The queryset of Voucher instances.
    - `serializer_class`: VoucherSerializer - The serializer class for Voucher instances.
    """

    queryset: Any = Voucher.objects.all()  # type: Any
    serializer_class: VoucherSerializer = VoucherSerializer  # type: VoucherSerializer


class VoucherApiListView(generics.ListCreateAPIView):
    """
    API view for listing and creating VoucherApi instances.

    Attributes:
    - `queryset`: Queryset - The queryset of VoucherApi instances.
    - `serializer_class`: VoucherApiSerializer - The serializer class for VoucherApi instances.
    """

    queryset: Any = VoucherApi.objects.all()  # type: Any
    serializer_class: VoucherApiSerializer = VoucherApiSerializer  # type: VoucherApiSerializer


class VoucherApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific VoucherApi instance.

    Attributes:
    - `queryset`: Queryset - The queryset of VoucherApi instances.
    - `serializer_class`: VoucherApiSerializer - The serializer class for VoucherApi instances.
    """

    queryset: Any = VoucherApi.objects.all()  # type: Any
    serializer_class: VoucherApiSerializer = VoucherApiSerializer  # type: VoucherApiSerializer
