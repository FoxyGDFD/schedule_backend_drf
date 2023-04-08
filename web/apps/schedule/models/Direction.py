from django.db import models
from .DirectionTrainingType import DirectionTrainingType


class Direction(models.Model):
    name = models.TextField(max_length=512, null=False, blank=False, unique=True)
    code = models.CharField(max_length=8, null=False, blank=False, unique=True)
    training_type = models.ForeignKey(DirectionTrainingType, on_delete=models.CASCADE, null=False, blank=False)
