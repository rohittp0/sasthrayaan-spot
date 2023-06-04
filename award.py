from config.models import GmailUser

for user in GmailUser.objects.filter(date_joined__day=24).exclude(institution__iexact="NSS"):
    print((f"{user.first_name} {user.last_name}", user.email))

    user.is_staff = True
    user.groups.add(1)
    user.save()

