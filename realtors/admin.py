from django.contrib import admin

# Register your models here.
from realtors.models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'phone', 'email', 'hire_date', 'is_mvp')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')

admin.site.register(Realtor, RealtorAdmin)