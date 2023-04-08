from django.db import models


class LessonNumber(models.Model):
    number = models.IntegerField(unique=True, blank=False, null=False)
    start_time = models.TimeField(unique=True, blank=False, null=False)
    end_time = models.TimeField(unique=True, blank=False, null=False)
