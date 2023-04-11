from django.db import models


class Faculty(models.Model):
    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    name = models.CharField(verbose_name='Название', max_length=512, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.name
