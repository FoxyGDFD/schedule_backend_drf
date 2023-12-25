from django.db import models
from .Group import Group
from .Classroom import Classroom
from .Subject import Subject
from .Teacher import Teacher


class Exam(models.Model):
    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"

    group = models.ManyToManyField(Group, verbose_name='Группа', blank=False, null=False)
    date_and_time = models.DateTimeField(verbose_name='Дата и время проведения', blank=False, null=False)
    classroom = models.ForeignKey(Classroom, verbose_name='Аудитория', on_delete=models.CASCADE, blank=False, null=False)
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE, blank=False, null=False)
    teacher = models.ManyToManyField(Teacher, verbose_name='Преподаватель', blank=False, null=False)
    
    def __str__(self):
        teachers = [f"{item[0]} {item[1][0]}. {item[2][0]}." for item in self.teacher.values_list('surname', 'name', 'patronymic')]
        return f'{self.date_and_time} {self.group.name} {self.subject} {self.classroom.name}' + ', '.join(teachers)
