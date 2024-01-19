from django.shortcuts import render, redirect
from dashboard.views import DashboardView
from .forms import VoucherRedemptionForm
from .services import VoucherRedemptionService
from voucher_management.services import VoucherManagementService
from django.http import HttpRequest
from django.contrib.auth.models import User
from typing import Any, Dict, List, Optional


class VoucherRedemptionView(DashboardView):
    """
    View for handling voucher redemption.

    Attributes:
    - `template`: str - Template name for the voucher redemption views.
    - `voucher_history_field_names`: List[str] - List of field names for voucher history display.
    - `form`: VoucherRedemptionForm - Form for redeeming vouchers.
    - `voucher_redemption_service`: VoucherRedemptionService - Instance of VoucherRedemptionService.
    - `voucher_management_service`: VoucherManagementService - Instance of VoucherManagementService.
    - `base_context`: Dict[str, Any] - Base context data for voucher redemption views.
    """
    template: str = 'voucher_redemption/base.html'
    voucher_history_field_names: List[str] = ['Code', 'Description', 'Discount %', 'Redeemed At']
    form: VoucherRedemptionForm = VoucherRedemptionForm()
    voucher_redemption_service: VoucherRedemptionService = VoucherRedemptionService()
    voucher_management_service: VoucherManagementService = VoucherManagementService()
    base_context: Dict[str, Any] = {
        'application_name': 'Voucher Redemption',
        'voucher_history_field_names': voucher_history_field_names,
    }

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> render:
        """
        Handle GET requests for voucher redemption.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - render: Rendered HTML response.
        """
        user: User = request.user
        redeemed_vouchers: List[Dict[str, Any]] = self.voucher_redemption_service.get_redeemed_vouchers(user)
        context: Dict[str, Any] = {
            'form': self.form,
            'redeemed_vouchers': redeemed_vouchers,
        }
        context.update(self.dashboard_context)
        context.update(self.base_context)
        return render(request, self.template, context)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> redirect:
        """
        Handle POST requests for redeeming vouchers.

        Parameters:
        - `request`: HttpRequest - The request object.

        Returns:
        - redirect: Redirect to the voucher redemption view.
        """
        voucher_code: Optional[str] = request.POST.get('code', None)
        user: User = request.user
        voucher: Optional[Dict[str, Any]] = self.voucher_management_service.get_voucher_by_code(voucher_code)
        if voucher:
            self.voucher_redemption_service.redeem_voucher(request, user, voucher)
        return redirect('redeem_voucher')
