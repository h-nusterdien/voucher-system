from django.http import HttpResponse
from .models import Voucher
from voucher_redemption.services import VoucherRedemptionService
import requests


class VoucherManagementService:
    voucher_redemption_service = VoucherRedemptionService()
    
    def get_voucher(self, id):
        voucher = None
        if id:
            try:
                voucher = Voucher.objects.get(id=id)
            except Voucher.DoesNotExist:
                return voucher
        return voucher
    
    def get_voucher_by_code(self, voucher_code):
        voucher = None
        if voucher_code:
            try:
                voucher = Voucher.objects.get(code__iexact=voucher_code)
            except Voucher.DoesNotExist:
                return voucher
        return voucher

    def update_voucher(self, voucher, form):
        changed_data_fields = form.changed_data
        form_cleaned_data = form.cleaned_data
        fields_to_be_updated = {}
        try:
            for changed_data_field in changed_data_fields: 
                fields_to_be_updated[changed_data_field] = form_cleaned_data.get(changed_data_field)
            voucher.code = fields_to_be_updated.get('code', voucher.code)
            voucher.description = fields_to_be_updated.get('description', voucher.description)
            voucher.discount_percentage = fields_to_be_updated.get('discount_percentage', voucher.discount_percentage)
            voucher.expiration_date = fields_to_be_updated.get('expiration_date', voucher.expiration_date)
            voucher.redemption_type = fields_to_be_updated.get('redemption_type', voucher.redemption_type)
            voucher.redemption_limit = self.voucher_redemption_service.get_redemption_limit(form)
            voucher.redemption_count = fields_to_be_updated.get('redemption_count', voucher.redemption_count)
            voucher.is_active = fields_to_be_updated.get('is_active', voucher.is_active)
        except:
            return False
        voucher.save()
        return True

    def create_voucher(self, form):
        form_data = form.cleaned_data
        redemption_type = form_data.get('redemption_type')
        redemption_limit = self.voucher_redemption_service.get_redemption_limit(form)
        try:
            Voucher.objects.create(
                code = form_data.get('code'),
                discount_percentage = form_data.get('discount_percentage'),
                description = form_data.get('description'),
                redemption_type = redemption_type,
                redemption_limit = redemption_limit,
                expiration_date = form_data.get('expiration_date'),
            )
        except Exception as e:
            return False
        return True

    def delete_voucher(self, voucher):
        try:
            api_url = f'http://127.0.0.1:8000/api/vouchers/{voucher.id}/'
            response = requests.delete(api_url)
            if response.status_code == 204:
                return HttpResponse(f'Successfully Deleted Voucher')
            else:
                return HttpResponse(f'Failed to Delete Voucher')
        except requests.exceptions.RequestException as e:
            return HttpResponse(f'API DELETE Request Error: {e}')
