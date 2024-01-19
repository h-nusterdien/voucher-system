from django.contrib import admin
from . import models

class VoucherAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Voucher)
