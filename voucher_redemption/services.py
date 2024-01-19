from django.contrib import messages
from .models import Voucher, VoucherRedemption


class VoucherRedemptionService():
    """
    Service class for handling voucher redemption operations.

    Methods:
    - `is_redeemable`: Checks if a voucher is redeemable based on its redemption limit and status.
    - `has_been_redeemed`: Checks if a user has already redeemed a specific voucher.
    - `get_redeemed_vouchers`: Retrieves a list of vouchers redeemed by a specific user.
    - `get_redemption_limit`: Determines the redemption limit based on the voucher redemption type.
    - `create_voucher_redemption`: Creates a new voucher redemption record for a user.
    - `redeem_voucher`: Redeems a voucher for a user, updating the redemption count and creating a redemption record.
    """

    def is_redeemable(self, voucher):
        """
        Checks if a voucher is redeemable based on its redemption limit and status.

        Parameters:
        - `voucher`: Voucher - The voucher object to check.

        Returns:
        - bool: True if the voucher is redeemable, False otherwise.
        """
        redemption_count = voucher.redemption_count
        redemption_limit = voucher.redemption_limit
        is_active = voucher.is_active
        if is_active and redemption_count < redemption_limit:
            return True
        return False
    
    def has_been_redeemed(self, user, voucher):
        """
        Checks if a user has already redeemed a specific voucher.

        Parameters:
        - `user`: User - The user object to check.
        - `voucher`: Voucher - The voucher object to check.

        Returns:
        - bool: True if the voucher has been redeemed by the user, False otherwise.
        """
        user_redeemed_vouchers = self.get_redeemed_vouchers(user)
        if voucher in user_redeemed_vouchers:
            return True
        return False

    def get_redeemed_vouchers(self, user):
        """
        Retrieves a list of vouchers redeemed by a specific user.

        Parameters:
        - `user`: User - The user object for which to retrieve redeemed vouchers.

        Returns:
        - QuerySet: List of vouchers redeemed by the user.
        """
        try:
            redeemed_vouchers = VoucherRedemption.objects.filter(user=user)
        except Exception as e:
            pass
        return redeemed_vouchers
    
    def get_redemption_limit(self, form):
        """
        Determines the redemption limit based on the voucher redemption type.

        Parameters:
        - `form`: Form - The form containing voucher redemption information.

        Returns:
        - int or None: Redemption limit value or None if not applicable.
        """
        form_data = form.cleaned_data
        redemption_type = form_data.get('redemption_type')
        x_times_redemption_limit = form_data.get('x_times_redemption_limit')
        if redemption_type == "x_times" and x_times_redemption_limit:
            return x_times_redemption_limit 
        elif redemption_type == "single":
                return 1
        return None
    
    def create_voucher_redemption(self, user, voucher):
        """
        Creates a new voucher redemption record for a user.

        Parameters:
        - `user`: User - The user redeeming the voucher.
        - `voucher`: Voucher - The voucher being redeemed.
        """
        VoucherRedemption.objects.create(
            user=user,
            voucher=voucher,
        )
        voucher.redemption_count += 1
        voucher.save()

    def redeem_voucher(self, request, user, voucher):
        """
        Redeems a voucher for a user, updating the redemption count and creating a redemption record.

        Parameters:
        - `request`: HttpRequest - The HTTP request.
        - `user`: User - The user redeeming the voucher.
        - `voucher`: Voucher - The voucher being redeemed.
        """
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
