from django.db import models
from .Direction import Direction


class Group(models.Model):
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    сourses = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    ]

    name = models.CharField(verbose_name='Название',
                            max_length=256, unique=True, null=False, blank=False)
    course = models.IntegerField(
        verbose_name='Курс', blank=False, null=False, choices=сourses, default=1)
    group = models.ForeignKey('self', verbose_name='Группа-родитель',
                              related_name='subgroups', on_delete=models.CASCADE, null=True, blank=True)
    direction = models.ForeignKey(
        Direction, verbose_name='Направление', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name
