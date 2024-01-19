from django.contrib import admin
from . import models

class VoucherRedemptionAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.VoucherRedemption)
