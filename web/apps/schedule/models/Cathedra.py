from django.db import models


class Cathedra(models.Model):
    name = models.CharField(max_length=512, blank=False, null=False, unique=True)
