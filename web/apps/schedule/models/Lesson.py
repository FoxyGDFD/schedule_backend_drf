from django.db import models
from .LessonNumber import LessonNumber
from .Teacher import Teacher
from .Subject import Subject
from .Classroom import Classroom
from .LessonType import LessonType
from .Group import Group


class Lesson(models.Model):
    class Meta:
        verbose_name = "Пара"
        verbose_name_plural = "Пары"

    number = models.ForeignKey(LessonNumber, verbose_name='Номер пары',  on_delete=models.CASCADE, blank=False, null=False)
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель', on_delete=models.CASCADE, blank=False, null=False)
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE, blank=False, null=False)
    classroom = models.ForeignKey(Classroom, verbose_name='Аудитория', on_delete=models.CASCADE, blank=False, null=False)
    lesson_type = models.ForeignKey(LessonType, verbose_name='Тип пары', on_delete=models.CASCADE, blank=False, null=False)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.lesson_type.name + self.subject.name + self.teacher.name +  self.teacher.surname + self.teacher.patronymic