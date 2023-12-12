from django.db import models
from .Cathedra import Cathedra


class Direction(models.Model):
    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

    training_types = [
        ('BACHELOUR', 'Бакалавриат'),
        ('SPESIALIST', 'Специалитет'),
        ('MAGISTRASY', 'Магистратура'),
        ('POSTGRADUETE', 'Аспирантура')
    ]

    name = models.TextField(verbose_name='Название',
                            max_length=512, null=False, blank=False, unique=True)
    code = models.CharField(verbose_name='Код направления',
                            max_length=8, null=False, blank=False, unique=True)
    training_type = models.CharField(
        verbose_name='Уровень обучения', choices=training_types, null=False, blank=False, max_length=12)

    cathedra = models.ForeignKey(
        Cathedra, verbose_name='Кафедра', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        srt_training_type = next(tr_type[1] for tr_type in self.training_types if tr_type[0] == self.training_type)
        return f'{srt_training_type}-{self.name}'
