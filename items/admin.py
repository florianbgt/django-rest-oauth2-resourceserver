from django.contrib import admin        #new

from .models import Item        #new


class ItemAdmin(admin.ModelAdmin):        #new
    pass        #new

admin.site.register(Item, ItemAdmin)        #new