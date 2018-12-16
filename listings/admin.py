from django.contrib import admin
from listings.models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'realtor')
    list_filter = ('realtor',)
    list_editable = ('is_published', 'price')
    list_per_page = 15
    search_fields = ('title', 'price', 'realtor__name')
admin.site.register(Listing, ListingAdmin)
