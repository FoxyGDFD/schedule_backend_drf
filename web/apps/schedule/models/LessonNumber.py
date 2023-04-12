from django.db import models


class LessonNumber(models.Model):
    class Meta:
        verbose_name = "Номер пары"
        verbose_name_plural = "Номера пар"

    number = models.IntegerField(verbose_name='Порядковый номер пары', unique=True, blank=False, null=False)
    start_time = models.TimeField(verbose_name='Время начала', unique=True, blank=False, null=False)
    end_time = models.TimeField(verbose_name='Время окончания', unique=True, blank=False, null=False)
    
    def __str__(self):
        return str(self.number) + 'я' + ' пара'
