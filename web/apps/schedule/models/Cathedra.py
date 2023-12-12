from django.db import models
from .Faculty import Faculty


class Cathedra(models.Model):
    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

    name = models.CharField(verbose_name='Название кафедры',
                            max_length=512, blank=False, null=False, unique=True)

    faculty = models.ForeignKey(
        Faculty, verbose_name='Факультет', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
