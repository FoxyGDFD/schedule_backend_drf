from django.db import models


class Cathedra(models.Model):
    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"
    
    name = models.CharField(verbose_name='Название кафедры', max_length=512, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.name
