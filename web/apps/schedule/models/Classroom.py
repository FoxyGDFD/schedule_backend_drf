from django.db import models


class Classroom(models.Model):
    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"

    name = models.CharField(verbose_name='Название',
                            max_length=128, blank=False, null=False)

    def __str__(self):
        return self.name
