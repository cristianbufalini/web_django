from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class NewUser(AbstractUser):
    is_superuser = models.BooleanField(default = False)
    is_writer = models.BooleanField(default = False)
    is_reader = models.BooleanField(default = True)
    birthday = models.DateField(null=True, default=None)