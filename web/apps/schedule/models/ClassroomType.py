from django.db import models


class ClassroomType(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False, unique=True)
