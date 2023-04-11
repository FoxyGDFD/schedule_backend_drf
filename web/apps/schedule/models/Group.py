from django.db import models
from .Direction import Direction


class Group(models.Model):
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    name = models.CharField(verbose_name='Название', max_length=256, unique=True, null=False, blank=False)
    course = models.IntegerField(verbose_name='Курс')
    group = models.ForeignKey('self', verbose_name='Группа-родитель', related_name='subgroups', on_delete=models.CASCADE, null=True, blank=False)
    direction = models.ForeignKey(Direction, verbose_name='Направление', on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return self.name
