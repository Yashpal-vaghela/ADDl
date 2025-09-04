from django.contrib import admin
from .models import Contact, HomeContact
from import_export.admin import ImportExportModelAdmin

# Admin display
class ContactAdmin(ImportExportModelAdmin):
    list_display = ['name', 'email', 'contact', 'message']
    search_fields = ['name', 'email', 'contact']

class HomeContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']

# Register models
admin.site.register(Contact, ContactAdmin)
admin.site.register(HomeContact, HomeContactAdmin)
