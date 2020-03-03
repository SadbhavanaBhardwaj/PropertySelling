from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'create_date', 'realtor')
    list_display_links = ('title', 'id')
    list_filter = ('realtor', )
    list_editable = ('is_published', )
    search_fields = ('title', 'id', 'address', 'zip_code', 'city', 'state')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
