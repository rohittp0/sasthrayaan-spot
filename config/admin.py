from allauth.socialaccount.models import SocialAccount
from django.contrib import admin
from django.utils.html import format_html

from config.models import GmailUser


# Register your models here.

class GmailUserAdmin(admin.ModelAdmin):
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

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
            return ' '.join(groups)

    group.short_description = 'Groups'

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
            return list_display + ('username', 'is_staff', 'group', 'institution')
        else:
            return list_display + ('phone', 'institution')

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return 'is_staff', 'groups', 'type', 'institution'
        else:
            return 'type', "institution"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(is_staff=False, is_superuser=False)


admin.site.register(GmailUser, GmailUserAdmin)
