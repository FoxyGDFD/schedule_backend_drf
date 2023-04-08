from django.db import models
from .Housing import Housing
from .ClassroomType import ClassroomType


class Classroom(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    floor = models.IntegerField(blank=False, null=False)
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, blank=False, null=False)
    classroom_type = models.ForeignKey(ClassroomType, on_delete=models.SET_NULL, blank=False, null=True)
