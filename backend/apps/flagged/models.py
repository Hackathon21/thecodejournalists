from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class FlaggedSite(models.Model):
    site = models.URLField(max_length=200)
    count = models.IntegerField(default=0)
    