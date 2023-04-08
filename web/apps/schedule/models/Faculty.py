from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False, unique=True)
