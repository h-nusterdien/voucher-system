from django.shortcuts import render, redirect
from django.contrib import messages
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
        context = {
            'form': self.create_voucher_form,
            'vouchers': vouchers,
        }
        context.update(self.base_context)
        context.update(self.dashboard_context)
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        form = CreateVoucherForm(request.POST)
        if form.is_valid():
            success = self.voucher_management_service.create_voucher(form)
            if success:
                success_message = f'Successfully Created Voucher'
                messages.success(request, success_message)
            else:
                error_message = f'Failed to Create Voucher'
                messages.error(request, error_message)
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
        context = {
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
        voucher = self.voucher_management_service.get_voucher(voucher_id)
        form_method = request.POST.get('formMethod')

        if form_method == 'PUT':
            form = UpdateVoucherForm(request.POST)
            if form.is_valid():
                success = self.voucher_management_service.update_voucher(voucher, form)
                if success:
                    messages.success(request, f'Successfully Updated Voucher')
                else:
                    messages.error(request, f'Failed to Update Voucher')
        elif form_method == 'DELETE':
            success = self.voucher_management_service.delete_voucher(voucher)
            if success:
                messages.success(request, f'Successfully Deleted Voucher')
            else:
                messages.error(request, f'Failed to Delete Voucher')

        return redirect('voucher_list')
