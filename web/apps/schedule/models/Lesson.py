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

    day = [
        ("monday", "Понедельник"),
        ("tuesda", "Вторник"),
        ("wednesda", "Среда"),
        ("thursda", "Четверг"),
        ("friday", "Пятница"),
        ("saturday", "Суббота"),
    ]

    number = models.ForeignKey(LessonNumber, verbose_name='Номер пары', on_delete=models.CASCADE, blank=False, null=False)
    teacher = models.ManyToManyField(Teacher, verbose_name='Преподаватель', blank=False, null=False, related_name='teacher')
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE, blank=False, null=False, related_name='subject')
    classroom = models.ForeignKey(Classroom, verbose_name='Аудитория', on_delete=models.CASCADE, blank=False, null=False, related_name='classroom')
    lesson_type = models.ForeignKey(LessonType, verbose_name='Тип пары', on_delete=models.CASCADE, blank=False, null=False, related_name='lesson_type')
    group = models.ManyToManyField(Group, verbose_name='Группа', blank=False, null=False)
    week_day = models.CharField(verbose_name="День недели", blank=False, null=False, choices=day, max_length=9, default="monday")

    def __str__(self):
        teachers = [f"{item[0]} {item[1][0]}. {item[2][0]}." for item in self.teacher.values_list('surname', 'name', 'patronymic')]
        week_day_value = next(temp_wd[1] for temp_wd in self.day if temp_wd[0] == self.week_day)
        return f'{week_day_value} {self.number}: {self.subject.name}, {self.lesson_type.name.lower()}, ' + ', '.join(teachers)

