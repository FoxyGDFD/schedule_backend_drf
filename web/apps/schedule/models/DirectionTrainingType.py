from django.db import models


class DirectionTrainingType(models.Model):
    class Meta:
        verbose_name = "Уровень направления подготовки"
        verbose_name_plural = "Уровни направления подготовки"

    name = models.CharField(verbose_name='Название', max_length=128, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.name
