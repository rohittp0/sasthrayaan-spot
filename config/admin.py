from allauth.socialaccount.models import SocialAccount
from django.contrib import admin
from django.utils.html import format_html

from config.models import GmailUser


# Register your models here.

class GmailUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'type')
    list_filter = ('type', "institution")
    search_fields = ('first_name', "last_name", 'email')
    readonly_fields = ('image_tag', 'email', 'username', 'name')

    model = GmailUser

    @staticmethod
    def name(obj):
        return obj.get_full_name()

    def image_tag(self, obj):
        src = SocialAccount.objects.get(user=obj).extra_data['picture']
        return format_html(f'<img src="{src}" />')

    image_tag.short_description = 'Image'

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        else:
            return (
                (None, {
                    'fields': ('image_tag', 'email', 'name', 'phone', 'type', 'institution')
                }),
            )

    def get_list_display(self, request, obj=None):
        list_display = ('name', 'email', 'type')

        if request.user.is_superuser:
            return list_display + ('username', 'is_staff', 'groups', 'institution')
        else:
            return list_display + ('phone', 'institution')


admin.site.register(GmailUser, GmailUserAdmin)
