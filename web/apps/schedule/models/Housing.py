from django.db import models


class Housing(models.Model):
    class Meta:
        verbose_name = "Корпус"
        verbose_name_plural = "Корпуса"

    name = models.CharField(verbose_name='Название', max_length=256, blank=False, null=False, unique=True)
    floors_quantity = models.IntegerField(verbose_name='Количество этажей', blank=False, null=False)
    
    def __str__(self):
        return self.name
