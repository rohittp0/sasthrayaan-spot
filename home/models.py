from django.db import models
from django.contrib.auth.models import AbstractUser


class Poster(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
