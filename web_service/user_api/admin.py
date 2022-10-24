from django.contrib import admin

from user_api.models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address')
    list_per_page = 25
    raw_id_fields = ('user',)


admin.site.register(Address, AddressAdmin)
