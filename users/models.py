from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)