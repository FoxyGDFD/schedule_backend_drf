from django.db import models
from .Housing import Housing
from .ClassroomType import ClassroomType


class Classroom(models.Model):
    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"

    name = models.CharField(verbose_name='Название', max_length=128, blank=False, null=False)
    floor = models.IntegerField(verbose_name='Этаж', blank=False, null=False)
    housing = models.ForeignKey(Housing, verbose_name='Корпус',  on_delete=models.CASCADE, blank=False, null=False)
    classroom_type = models.ForeignKey(ClassroomType, verbose_name='Тип', on_delete=models.SET_NULL, blank=False, null=True)
    
    def __str__(self):
        return self.name + self.housing.name
