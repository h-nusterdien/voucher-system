from django.contrib import messages
from .models import Voucher, VoucherRedemption


class VoucherRedemptionService():

    def is_redeemable(self, voucher):
        redemption_count = voucher.redemption_count
        redemption_limit = voucher.redemption_limit
        is_active = voucher.is_active
        if is_active and redemption_count < redemption_limit:
            return True
        return False
    
    def has_been_redeemed(self, user, voucher):
        user_redeemed_vouchers = self.get_redeemed_vouchers(user)
        if voucher in user_redeemed_vouchers:
            return True
        return False

    def get_redeemed_vouchers(self, user):
        try:
            redeemed_vouchers = VoucherRedemption.objects.filter(user=user)
        except Exception as e:
            pass
        return redeemed_vouchers
    
    def get_redemption_limit(self, form):
        form_data = form.cleaned_data
        redemption_type = form_data.get('redemption_type')
        x_times_redemption_limit = form_data.get('x_times_redemption_limit')
        if redemption_type == "x_times" and x_times_redemption_limit:
            return x_times_redemption_limit 
        elif redemption_type == "single":
                return 1
        return None
    
    def create_voucher_redemption(self, user, voucher):
        VoucherRedemption.objects.create(
            user=user,
            voucher=voucher,
        )
        voucher.redemption_count += 1
        voucher.save()

    def redeem_voucher(self, request, user, voucher):
        form_voucher_code = request.POST.get("code")
        if voucher:
            has_been_redeemed = self.has_been_redeemed(user, voucher)
            if not has_been_redeemed:
                is_redeemable = self.is_redeemable(voucher)
                if is_redeemable:
                    self.create_voucher_redemption(user, voucher)
                    alert_message = f'Voucher "{form_voucher_code}" successfully redeemed '
                    messages.success(request, alert_message)
                else:
                    alert_message = f'Voucher "{form_voucher_code}" cannot be redeemed'
                    messages.info(request, alert_message)
            else:
                alert_message = f'Voucher "{form_voucher_code}" has already been redeemed'
                messages.info(request, alert_message)
        else:
            alert_message = f'Voucher "{form_voucher_code}" does not exist!'
            messages.error(request, alert_message)
