from django.contrib import admin

from config.models import GmailUser


# Register your models here.

class GmailUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'type')
    list_filter = ('type',)
    search_fields = ('name', 'email', 'type')
    model = GmailUser
