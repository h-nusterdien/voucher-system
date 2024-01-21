from django.shortcuts import render, redirect
from dashboard.views import DashboardView
from .models import Voucher
from .forms import CreateVoucherForm, UpdateVoucherForm
from .services import VoucherManagementService


class VoucherManagementView(DashboardView):
    """
    Base view for voucher management, providing common functionalities and templates.

    Attributes:
    - `template`: The template file to be used for rendering.
    - `voucher_field_names`: List of field names for displaying voucher details.
    - `voucher_management_service`: An instance of the VoucherManagementService for managing vouchers.
    - `base_context`: Base context containing application name and voucher field names.
    """

    template = 'voucher_management/base.html'
    voucher_field_names = [
        'Code', 'Description', 'Discount %', 'Redemption Type', 'Redemption Limit', 'Redemption Count', 'Expiry Date', 'Status', 'Action'
    ]
    voucher_management_service = VoucherManagementService()
    base_context = {
        'application_name': 'Voucher Management',
        'voucher_field_names': voucher_field_names,
    }


class VoucherManagementListView(VoucherManagementView):
    """
    View for listing vouchers and handling voucher creation.

    Attributes:
    - `create_voucher_form`: Form for creating a new voucher.
    """

    create_voucher_form = CreateVoucherForm()

    def get(self, request, *args, **kwargs):
        vouchers = Voucher.objects.all()
        user = request.user
        voucher_management_access = user.is_staff or user.is_superuser
        context = {
            'voucher_management_access': voucher_management_access,
            'form': self.create_voucher_form,
            'vouchers': vouchers,
        }
        context.update(self.base_context)
        context.update(self.dashboard_context)
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        self.voucher_management_service.create_voucher(request)
        return redirect('voucher_list')


class VoucherManagementDetailView(VoucherManagementView):
    """
    View for displaying details of a specific voucher, handling voucher updates, and deletions.

    Attributes:
    - `update_voucher_form`: Form for updating voucher details.
    """

    update_voucher_form = UpdateVoucherForm()

    def get(self, request, *args, **kwargs):
        voucher_id = kwargs.get('pk', None)
        voucher = self.voucher_management_service.get_voucher(voucher_id)
        user = request.user
        voucher_management_access = user.is_staff or user.is_superuser
        context = {
            'voucher_management_access': voucher_management_access,
            'form': self.update_voucher_form,
            'voucher_detail_view': True,
            'voucher_detail_view_url': f'/portal/voucher-management/vouchers/{voucher_id}/',
            'csrf_token': request.COOKIES['csrftoken'],
            'vouchers': [voucher],
        }
        context.update(self.base_context)
        context.update(self.dashboard_context)
        return render(request, self.template, context)
    
    def post(self, request, *args, **kwargs):
        voucher_id = kwargs.get('pk', None)
        form_method = request.POST.get('formMethod')
        if form_method == 'PUT':
           self.voucher_management_service.update_voucher(request, voucher_id)
        elif form_method == 'DELETE':
            self.voucher_management_service.delete_voucher(request, voucher_id)
        return redirect('voucher_detail', voucher_id)
