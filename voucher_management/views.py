from django.shortcuts import render, redirect
from django.contrib import messages
from dashboard.views import DashboardView
from .models import Voucher
from .forms import CreateVoucherForm, UpdateVoucherForm
from .services import VoucherManagementService
from django.http import HttpRequest, HttpResponse
from typing import Any, Dict, List

class VoucherManagementView(DashboardView):
    """
    Base class for voucher management views.

    Attributes:
    - `template`: str - Template name for the voucher management views.
    - `voucher_field_names`: List[str] - List of field names for voucher display.
    - `voucher_management_service`: VoucherManagementService - Instance of VoucherManagementService.
    - `base_context`: Dict[str, Any] - Base context data for voucher management views.
    """
    template: str = 'voucher_management/base.html'
    voucher_field_names: List[str] = [
        'Code', 'Description', 'Discount %', 'Redemption Type', 'Redemption Limit', 'Redemption Count', 'Expiry Date', 'Status', 'Action'
    ]
    voucher_management_service: VoucherManagementService = VoucherManagementService()
    base_context: Dict[str, Any] = {
        'application_name': 'Voucher Management',
        'voucher_field_names': voucher_field_names,
    }

class VoucherManagementListView(VoucherManagementView):
    """
    View for listing vouchers and creating new vouchers.

    Attributes:
    - `create_voucher_form`: CreateVoucherForm - Form for creating vouchers.
    """
    create_voucher_form: CreateVoucherForm = CreateVoucherForm()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> render:
        """
        Handle GET requests for voucher listing.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - render: Rendered HTML response.
        """
        vouchers: List[Voucher] = Voucher.objects.all()
        context: Dict[str, Any] = {
            'form': self.create_voucher_form,
            'vouchers': vouchers,
        }
        context.update(self.base_context)
        context.update(self.dashboard_context)
        return render(request, self.template, context)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> redirect:
        """
        Handle POST requests for creating new vouchers.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - redirect: Redirect to the voucher list view.
        """
        form: CreateVoucherForm = CreateVoucherForm(request.POST)
        if form.is_valid():
            success: bool = self.voucher_management_service.create_voucher(form)
            if success:
                messages.success(request, 'Successfully Created Voucher')
            else:
                messages.error(request, 'Failed to Create Voucher')
        return redirect('voucher_list')


class VoucherManagementDetailView(VoucherManagementView):
    """
    View for displaying and updating voucher details.

    Attributes:
    - `update_voucher_form`: UpdateVoucherForm - Form for updating vouchers.
    """
    update_voucher_form: UpdateVoucherForm = UpdateVoucherForm()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> render:
        """
        Handle GET requests for voucher details.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - render: Rendered HTML response.
        """
        voucher_id: int = kwargs.get('pk', None)
        voucher: Voucher = self.voucher_management_service.get_voucher(voucher_id)
        context: Dict[str, Any] = {
            'form': self.update_voucher_form,
            'voucher_detail_view': True,
            'voucher_detail_view_url': f'/portal/voucher-management/vouchers/{voucher_id}/',
            'csrf_token': request.COOKIES['csrftoken'],
            'vouchers': [voucher],
        }
        context.update(self.base_context)
        context.update(self.dashboard_context)
        return render(request, self.template, context)
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> redirect:
        """
        Handle POST requests for updating or deleting vouchers.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - redirect: Redirect to the voucher list view.
        """
        voucher_id: int = kwargs.get('pk', None)
        voucher: Voucher = self.voucher_management_service.get_voucher(voucher_id)
        form_method: str = request.POST.get('formMethod')

        if form_method == 'PUT':
            form: UpdateVoucherForm = UpdateVoucherForm(request.POST)
            if form.is_valid():
                success: bool = self.voucher_management_service.update_voucher(voucher, form)
                if success:
                    messages.success(request, 'Successfully Updated Voucher')
                else:
                    messages.error(request, 'Failed to Update Voucher')
        elif form_method == 'DELETE':
            success: HttpResponse = self.voucher_management_service.delete_voucher(voucher)
            if 'Success' in success.content:
                messages.success(request, 'Successfully Deleted Voucher')
            else:
                messages.error(request, 'Failed to Delete Voucher')

        return redirect('voucher_list')
