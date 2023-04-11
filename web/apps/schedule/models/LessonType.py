from django.db import models


class LessonType(models.Model):
    class Meta:
        verbose_name = "Тип пары"
        verbose_name_plural = "Типы пар"

    name = models.CharField(verbose_name='Название', max_length=512, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.name
