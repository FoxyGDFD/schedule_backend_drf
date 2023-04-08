from django.db import models
from .Direction import Direction


class Group(models.Model):
    name = models.CharField(max_length=256, unique=True, null=False, blank=False)
    course = models.IntegerField()
    group = models.ForeignKey('self', related_name='subgroups', on_delete=models.CASCADE, null=True, blank=False)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=False, blank=False)
