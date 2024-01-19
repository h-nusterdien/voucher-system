from django.shortcuts import render, redirect
from dashboard.views import DashboardView
from .forms import VoucherRedemptionForm
from .services import VoucherRedemptionService
from voucher_management.services import VoucherManagementService


class VoucherRedemptionView(DashboardView):
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
        user = request.user
        redeemed_vouchers = self.voucher_redemption_service.get_redeemed_vouchers(user)
        context = {
            'form': self.form,
            'redeemed_vouchers': redeemed_vouchers,
        }
        context.update(self.dashboard_context)
        context.update(self.base_context)
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        voucher_code = request.POST.get('code', None)
        user = request.user
        voucher = self.voucher_management_service.get_voucher_by_code(voucher_code)
        self.voucher_redemption_service.redeem_voucher(request, user, voucher)
        return redirect('redeem_voucher')
