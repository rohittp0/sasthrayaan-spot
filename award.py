from config.models import GmailUser

for user in GmailUser.objects.filter(institution__iexact="NSS"):
    user.is_staff = True
    user.groups.add(1)
    user.save()
    
