from django.contrib import admin

from config.models import GmailUser


# Register your models here.

class GmailUserAdmin(admin.ModelAdmin):
    list_display = ("username", 'name', 'email', 'type')
    list_filter = ('type', "institution")
    search_fields = ('first_name', "last_name", 'email', 'type')
    model = GmailUser

    def name(self, obj):
        return obj.get_full_name()

    "remove some fields from the admin form only for other users than superuser"

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        else:
            return (
                (None, {
                    'fields': ('first_name', 'last_name', 'phone', 'type', 'institution')
                }),
            )


admin.site.register(GmailUser, GmailUserAdmin)
