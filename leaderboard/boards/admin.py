from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    fields = ['item_text', 'score']
    list_display = ('item_text', 'score', 'created')

# Register your models here.
admin.site.register(Item, ItemAdmin)
