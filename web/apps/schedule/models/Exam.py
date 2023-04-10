from django.db import models
from .Group import Group
from .Classroom import Classroom
from .Subject import Subject
from .Teacher import Teacher


class Exam(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=False, null=False)
    date_and_time = models.DateTimeField(blank=False, null=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=False)
