from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    alias = models.CharField(max_length=10, unique=True, primary_key=True)
    url = models.URLField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(null=True)

