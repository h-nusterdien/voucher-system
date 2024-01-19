from rest_framework import generics
from .models import Voucher, VoucherApi
from .serializers import VoucherSerializer, VoucherApiSerializer


class VoucherAPIListView(generics.ListCreateAPIView):
    """
    API view for listing and creating Voucher objects.

    Attributes:
    - `queryset` (QuerySet): Set of Voucher objects.
    - `serializer_class` (Serializer): Serializer class for Voucher objects.
    """ 
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer


class VoucherAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific Voucher object.

    Attributes:
    - `queryset` (QuerySet): Set of Voucher objects.
    - `serializer_class` (Serializer): Serializer class for Voucher objects.
    """
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer


class VoucherApiListView(generics.ListCreateAPIView):
    """
    API view for listing and creating VoucherApi objects.

    Attributes:
    - `queryset` (QuerySet): Set of VoucherApi objects.
    - `serializer_class` (Serializer): Serializer class for VoucherApi objects.
    """
    queryset = VoucherApi.objects.all()
    serializer_class = VoucherApiSerializer


class VoucherApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific VoucherApi object.

    Attributes:
    - `queryset` (QuerySet): Set of VoucherApi objects.
    - `serializer_class` (Serializer): Serializer class for VoucherApi objects.
    """
    queryset = VoucherApi.objects.all()
    serializer_class = VoucherApiSerializer
