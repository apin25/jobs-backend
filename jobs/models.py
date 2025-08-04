from django.db import models
import uuid
# Create your models here.
class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    job_position = models.CharField(max_length=255, blank=False)
    type_of_workplace = models.CharField(max_length=255, blank=False)
    job_location = models.CharField(max_length=255, blank=False)
    company = models.CharField(max_length=255, blank=False)
    employment_type = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=2048, blank=False)
    close_at = models.DateTimeField(null=False)