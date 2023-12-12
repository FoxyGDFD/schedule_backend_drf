from django.db import models
from .Group import Group
from .Classroom import Classroom
from .Subject import Subject
from .Teacher import Teacher


class Exam(models.Model):
    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"

    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE, blank=False, null=False,)
    date_and_time = models.DateTimeField(verbose_name='Дата и время проведения', blank=False, null=False,)
    classroom = models.ForeignKey(Classroom, verbose_name='Аудитория', on_delete=models.CASCADE, blank=False, null=False,)
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE, blank=False, null=False,)
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель', on_delete=models.CASCADE, blank=False, null=False,)
    
    def __str__(self):
        return f'{self.date_and_time.date()} {self.group.name} {self.subject} {self.classroom.name} {self.teacher.surname} {self.teacher.name[0]}. {self.teacher.patronymic[0]}.'
