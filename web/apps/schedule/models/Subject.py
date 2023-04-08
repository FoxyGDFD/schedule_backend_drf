from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=512, blank=False, null=False, unique=True)
