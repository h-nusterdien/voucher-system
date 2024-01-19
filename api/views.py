from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Voucher, VoucherApi
from .serializers import VoucherSerializer, VoucherApiSerializer


class VoucherAPIListView(generics.ListCreateAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer


class VoucherAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer


class VoucherApiListView(generics.ListCreateAPIView):
    queryset = VoucherApi.objects.all()
    serializer_class = VoucherApiSerializer


class VoucherApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VoucherApi.objects.all()
    serializer_class = VoucherApiSerializer
