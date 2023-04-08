from django.db import models
from .LessonNumber import LessonNumber
from .Teacher import Teacher
from .Subject import Subject
from .Classroom import Classroom
from .LessonType import LessonType
from .Group import Group


class Lesson(models.Model):
    number = models.ForeignKey(LessonNumber, on_delete=models.CASCADE, blank=False, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=False)
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE, blank=False, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=False, null=False)
