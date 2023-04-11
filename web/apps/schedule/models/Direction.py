from django.db import models
from .DirectionTrainingType import DirectionTrainingType


class Direction(models.Model):
    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

    name = models.TextField(verbose_name='Название', max_length=512, null=False, blank=False, unique=True)
    code = models.CharField(verbose_name='Код направления', max_length=8, null=False, blank=False, unique=True)
    training_type = models.ForeignKey(DirectionTrainingType, verbose_name='Уровень обучения', on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return self.training_type.name + self.name
