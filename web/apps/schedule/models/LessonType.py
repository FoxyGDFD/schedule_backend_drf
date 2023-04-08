from django.db import models


class LessonType(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False, unique=True)
