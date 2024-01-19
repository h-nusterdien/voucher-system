from django.contrib import messages
from .models import Voucher, VoucherRedemption
from django.forms import Form
from django.http import HttpRequest
from django.contrib.auth.models import User
from typing import Any, Optional, List


class VoucherRedemptionService:
    """
    Service class for voucher redemption operations.

    Methods:
    - `is_redeemable`: Check if a voucher is redeemable based on its redemption count and limit.
    - `has_been_redeemed`: Check if a user has already redeemed a specific voucher.
    - `get_redeemed_vouchers`: Get a list of vouchers redeemed by a user.
    - `get_redemption_limit`: Get the redemption limit based on the redemption type in the form.
    - `create_voucher_redemption`: Create a voucher redemption record for a user.
    - `redeem_voucher`: Redeem a voucher for a user.
    """
    
    def is_redeemable(self, voucher: Voucher) -> bool:
        """
        Check if a voucher is redeemable.

        Parameters:
        - `voucher`: Voucher - The voucher instance.

        Returns:
        - bool: True if redeemable, False otherwise.
        """
        redemption_count: int = voucher.redemption_count
        redemption_limit: int = voucher.redemption_limit
        is_active: bool = voucher.is_active
        return is_active and redemption_count < redemption_limit if is_active else False
    
    def has_been_redeemed(self, user: User, voucher: Voucher) -> bool:
        """
        Check if a user has already redeemed a specific voucher.

        Parameters:
        - `user`: User - The user instance.
        - `voucher`: Voucher - The voucher instance.

        Returns:
        - bool: True if the voucher has been redeemed by the user, False otherwise.
        """
        user_redeemed_vouchers: List[VoucherRedemption] = self.get_redeemed_vouchers(user)
        return voucher in user_redeemed_vouchers
    
    def get_redeemed_vouchers(self, user: User) -> List[VoucherRedemption]:
        """
        Get a list of vouchers redeemed by a user.

        Parameters:
        - `user`: User - The user instance.

        Returns:
        - List[VoucherRedemption]: List of redeemed voucher instances.
        """
        try:
            redeemed_vouchers: List[VoucherRedemption] = VoucherRedemption.objects.filter(user=user)
        except Exception as e:
            redeemed_vouchers = []
        return redeemed_vouchers
    
    def get_redemption_limit(self, form: Form) -> Optional[int]:
        """
        Get the redemption limit based on the redemption type in the form.

        Parameters:
        - `form`: Form - The form instance.

        Returns:
        - Optional[int]: The redemption limit or None if not applicable.
        """
        form_data: Dict[str, Any] = form.cleaned_data
        redemption_type: str = form_data.get('redemption_type')
        x_times_redemption_limit: Optional[int] = form_data.get('x_times_redemption_limit')
        
        if redemption_type == "x_times" and x_times_redemption_limit:
            return x_times_redemption_limit 
        elif redemption_type == "single":
            return 1
        return None
    
    def create_voucher_redemption(self, user: User, voucher: Voucher) -> None:
        """
        Create a voucher redemption record for a user.

        Parameters:
        - `user`: User - The user instance.
        - `voucher`: Voucher - The voucher instance.
        """
        VoucherRedemption.objects.create(
            user=user,
            voucher=voucher,
        )
        voucher.redemption_count += 1
        voucher.save()

    def redeem_voucher(self, request: HttpRequest, user: User, voucher: Optional[Voucher]) -> None:
        """
        Redeem a voucher for a user.

        Parameters:
        - `request`: HttpRequest - The request object.
        - `user`: User - The user instance.
        - `voucher`: Optional[Voucher] - The voucher instance or None.
        """
        form_voucher_code: Optional[str] = request.POST.get("code")
        
        if voucher:
            has_been_redeemed: bool = self.has_been_redeemed(user, voucher)
            if not has_been_redeemed:
                is_redeemable: bool = self.is_redeemable(voucher)
                if is_redeemable:
                    self.create_voucher_redemption(user, voucher)
                    alert_message: str = f'Voucher "{form_voucher_code}" successfully redeemed '
                    messages.success(request, alert_message)
                else:
                    alert_message: str = f'Voucher "{form_voucher_code}" cannot be redeemed'
                    messages.info(request, alert_message)
            else:
                alert_message: str = f'Voucher "{form_voucher_code}" has already been redeemed'
                messages.info(request, alert_message)
        else:
            alert_message: str = f'Voucher "{form_voucher_code}" does not exist!'
            messages.error(request, alert_message)
