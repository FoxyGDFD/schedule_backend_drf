from django.db import models


class Housing(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False, unique=True)
    floors_quantity = models.IntegerField(blank=False, null=False)
