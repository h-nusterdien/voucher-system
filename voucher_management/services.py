from django.contrib import messages
from .models import Voucher
from .forms import CreateVoucherForm, UpdateVoucherForm
from voucher_redemption.services import VoucherRedemptionService


class VoucherManagementService:
    """
    Service class for managing voucher-related operations.

    Attributes:
    - `voucher_redemption_service`: An instance of VoucherRedemptionService for handling voucher redemption operations.
    """

    voucher_redemption_service = VoucherRedemptionService()

    def get_voucher(self, id):
        """
        Retrieve a voucher by its ID.

        Parameters:
        - `id` (int): The ID of the voucher to retrieve.

        Returns:
        - A Voucher instance if found, else None.
        """
        voucher = None
        if id:
            try:
                voucher = Voucher.objects.get(id=id)
            except Voucher.DoesNotExist:
                return voucher
        return voucher

    def get_voucher_by_code(self, voucher_code):
        """
        Retrieve a voucher by its unique code (case-insensitive).

        Parameters:
        - `voucher_code` (str): The unique code of the voucher.

        Returns:
        - A Voucher instance if found, else None.
        """
        voucher = None
        if voucher_code:
            try:
                voucher = Voucher.objects.get(code__iexact=voucher_code)
            except Voucher.DoesNotExist:
                return voucher
        return voucher
    
    def update_voucher(self, request, voucher_id):
        """
        Updates a voucher based on the provided voucher ID and form data.

        Args:
        - `request` (HttpRequest): The HTTP request object.
        - `voucher_id` (int): The ID of the voucher to be updated.

        Side Effects:
        - If the form is valid and the voucher is successfully updated, a success message is added to the Django messages framework.
        - If an exception occurs during the update process, an error message is added to the Django messages framework.
        - If the form is not valid, an info message is added to the Django messages framework.

        Note:
        - The update involves extracting and applying the changed fields from the form to the existing voucher.
        """
        form = UpdateVoucherForm(request.POST)
        if form.is_valid():
            form_cleaned_data = form.cleaned_data
            changed_data_fields = form.changed_data
            fields_to_be_updated = {}
            for changed_data_field in changed_data_fields: 
                fields_to_be_updated[changed_data_field] = form_cleaned_data.get(changed_data_field)
            try:
                voucher = self.get_voucher(voucher_id)
                voucher.code = fields_to_be_updated.get('code', voucher.code)
                voucher.description = fields_to_be_updated.get('description', voucher.description)
                voucher.discount_percentage = fields_to_be_updated.get('discount_percentage', voucher.discount_percentage)
                voucher.expiration_date = fields_to_be_updated.get('expiration_date', voucher.expiration_date)
                voucher.redemption_type = fields_to_be_updated.get('redemption_type', voucher.redemption_type)
                voucher.redemption_limit = self.voucher_redemption_service.get_redemption_limit(form)
                voucher.redemption_count = fields_to_be_updated.get('redemption_count', voucher.redemption_count)
                voucher.is_active = fields_to_be_updated.get('is_active', voucher.is_active)
                messages.success(request, f'Successfully Updated Voucher')
                voucher.save()
            except Exception as e:
                messages.error(request, f'Failed to Update Voucher')
        else:
            messages.info(request, f'Please retry submitting the form')

            
    def create_voucher(self, request):
        """
        Creates a new voucher based on the provided form data.

        Args:
        - `request` (HttpRequest): The HTTP request object.

        Side Effects:
        - If the form is valid and the voucher is successfully created, a success message is added to the Django messages framework.
        - If an exception occurs during the creation process, an error message is added to the Django messages framework.
        - If the form is not valid, an info message is added to the Django messages framework.

        Note:
        - The creation involves extracting relevant data from the form and attempting to create a new Voucher object.
        """
        form = CreateVoucherForm(request.POST)
        if form.is_valid():
            form_cleaned_data = form.cleaned_data
            redemption_type = form_cleaned_data.get('redemption_type')
            redemption_limit = self.voucher_redemption_service.get_redemption_limit(form)
            try:
                Voucher.objects.create(
                    code = form_cleaned_data.get('code'),
                    discount_percentage = form_cleaned_data.get('discount_percentage'),
                    description = form_cleaned_data.get('description'),
                    redemption_type = redemption_type,
                    redemption_limit = redemption_limit,
                    expiration_date = form_cleaned_data.get('expiration_date'),
                )
                messages.success(request, f'Successfully Created Voucher')
            except Exception as e:
                messages.error(request, f'Failed to Create Voucher')
        else:
            messages.info(request, f'Please retry submitting the form')

    def delete_voucher(self, request, voucher_id):
        """
        Deletes a voucher based on the provided voucher ID.

        Args:
        - `request` (HttpRequest): The HTTP request object.
        - `voucher_id` (int): The ID of the voucher to be deleted.

        Side Effects:
        - If the voucher is successfully deleted, a success message is added to the Django messages framework.
        - If an exception occurs during the deletion process, an error message is added to the Django messages framework.
        """
        try:
            voucher = self.get_voucher(voucher_id)
            voucher.delete()
            messages.success(request, f'Successfully Deleted Voucher')
        except Exception as e:
            messages.error(request, f'Failed to Delete Voucher')
