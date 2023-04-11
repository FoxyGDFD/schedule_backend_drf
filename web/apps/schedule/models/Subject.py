from django.db import models


class Subject(models.Model):

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    name = models.CharField(verbose_name='Название', max_length=512, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.name
