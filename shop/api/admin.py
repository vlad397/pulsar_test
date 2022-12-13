from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor_code', 'price', 'status',)
    list_filter = ('status',)
    search_fields = ('name', 'vendor_code', 'status',)


admin.site.register(Item, ItemAdmin)
