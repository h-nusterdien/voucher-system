from django.shortcuts import render, redirect
from dashboard.views import DashboardView
from .forms import VoucherRedemptionForm
from .services import VoucherRedemptionService
from voucher_management.services import VoucherManagementService


class VoucherRedemptionView(DashboardView):
    """
    View for handling voucher redemption functionalities.

    Attributes:
    - `template`: str - The template name for rendering the view.
    - `voucher_history_field_names`: list - Field names for displaying voucher history.
    - `form`: VoucherRedemptionForm - Form for voucher redemption.
    - `voucher_redemption_service`: VoucherRedemptionService - Service for voucher redemption.
    - `voucher_management_service`: VoucherManagementService - Service for voucher management.
    - `base_context`: dict - Base context for the view.

    Methods:
    - `get`: Handles GET requests, retrieves redeemed vouchers, and renders the redemption form.
    - `post`: Handles POST requests, redeems a voucher, and redirects to the redemption page.
    """

    template = 'voucher_redemption/base.html'
    voucher_history_field_names = ['Code', 'Description', 'Discount %', 'Redeemed At']
    form = VoucherRedemptionForm()
    voucher_redemption_service = VoucherRedemptionService()
    voucher_management_service = VoucherManagementService()

    base_context = {
        'application_name': 'Voucher Redemption',
        'voucher_history_field_names': voucher_history_field_names,
    }
    
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests, retrieves redeemed vouchers, and renders the redemption form.

        Parameters:
        - `request`: HttpRequest - The HTTP request.
        - `args`: Any - Variable-length argument list.
        - `kwargs`: Any - Arbitrary keyword arguments.

        Returns:
        - HttpResponse: Rendered response with voucher redemption form and redeemed vouchers.
        """
        user = request.user
        redeemed_vouchers = self.voucher_redemption_service.get_redeemed_vouchers(user)
        voucher_management_access = user.is_staff or user.is_superuser
        context = {
            'voucher_management_access': voucher_management_access,
            'form': self.form,
            'redeemed_vouchers': redeemed_vouchers,
        }
        context.update(self.dashboard_context)
        context.update(self.base_context)
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, redeems a voucher, and redirects to the redemption page.

        Parameters:
        - `request`: HttpRequest - The HTTP request.
        - `args`: Any - Variable-length argument list.
        - `kwargs`: Any - Arbitrary keyword arguments.

        Returns:
        - HttpResponse: Redirects to the voucher redemption page.
        """
        voucher_code = request.POST.get('code', None)
        user = request.user
        voucher = self.voucher_management_service.get_voucher_by_code(voucher_code)
        self.voucher_redemption_service.redeem_voucher(request, user, voucher)
        return redirect('redeem_voucher')
