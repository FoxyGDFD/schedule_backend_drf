from django.db import models


class ClassroomType(models.Model):
    class Meta:
        verbose_name = "Тип аудитории"
        verbose_name_plural = "Типы аудиторий"

    name = models.CharField(verbose_name='Название', max_length=256, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name