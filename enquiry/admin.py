from django.contrib import admin
from .models import Contact, ChatEnquiry
from import_export.admin import ImportExportModelAdmin

# Admin display
class ContactAdmin(ImportExportModelAdmin):
    list_display = ['name', 'email', 'contact', 'message']
    search_fields = ['name', 'email', 'contact']
    readonly_fields = ['created_at']
    list_filter = ['created_at']
    ordering = ['-created_at']

class ChatEnquiryAdmin(ImportExportModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']
    list_filter = ['created_at']
    ordering = ['-created_at']
    

# Register models
admin.site.register(Contact, ContactAdmin)
admin.site.register(ChatEnquiry, ChatEnquiryAdmin)
