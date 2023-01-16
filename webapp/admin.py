from django.contrib import admin

from .models import *

class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'city', 'bedrooms', 'rental_price', 'image')
    # list_display = ('__all__')

admin.site.register(Customer)
admin.site.register(House, HouseAdmin)
admin.site.register(Tag)
