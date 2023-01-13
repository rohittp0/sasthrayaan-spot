from django.contrib.auth.models import AbstractUser
from django.db import models

user_types = ["school-student", "undergraduate", "postgraduate", "research-scholar", "other"]

user_types = [(i, i.replace("-", " ").title()) for i in user_types]


class GmailUser(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, null=True)
    type = models.CharField(max_length=16, choices=user_types, default="other")
    institution = models.CharField(max_length=64, blank=True, null=True)
    phone_verified = models.BooleanField(default=False)
