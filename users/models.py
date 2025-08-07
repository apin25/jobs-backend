from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set', 
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set', 
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.utils import timezone

class ExpiringToken(Token):
    class Meta:
        proxy = True

    def expired(self):
        now = timezone.now()
        return self.created < now - timedelta(hours=24)
