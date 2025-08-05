from django.db import models
import uuid
# Create your models here.
class Job(models.Model):
    TYPE_OF_WORKPLACE = [
        ("On Site", "On Site"),
        ("Hybrid", "Hybrid"),
        ("Remote", "Remote")
    ]
    EMPLOYMENT_TYPE = [
        ("Full time", "Full time"),
        ("Part time", "Part time"),
        ("Contract", "Contract"),
        ("Temporary", "Temporary"),
        ("Volunteer", "Volunteer"),
        ("Apprenticeship", "Apprenticeship")
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    job_position = models.CharField(max_length=255, blank=False)
    type_of_workplace = models.CharField(max_length=255, blank=False, choices=TYPE_OF_WORKPLACE)
    job_location = models.CharField(max_length=255, blank=False)
    company = models.CharField(max_length=255, blank=False)
    employment_type = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=2048, blank=False)
    close_at = models.DateTimeField(null=False)