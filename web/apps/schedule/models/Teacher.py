from django.db import models
from .Cathedra import Cathedra


class Teacher(models.Model):
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    cathedra = models.ManyToManyField(
        Cathedra, verbose_name='Кафедра', blank=False, null=False)
    name = models.CharField(
        verbose_name='Имя', max_length=256, blank=False, null=False)
    surname = models.CharField(
        verbose_name='Фамилия', max_length=256, blank=False, null=False)
    patronymic = models.CharField(
        verbose_name='Отчество', max_length=256, blank=False, null=False)
    photo = models.ImageField(
        verbose_name='Фотография', null=True, blank=False)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
