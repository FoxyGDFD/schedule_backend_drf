from django.db import models
from .Faculty import Faculty


class Teacher(models.Model):
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=256, blank=False, null=False)
    surname = models.CharField(max_length=256, blank=False, null=False)
    patronymic = models.CharField(max_length=256, blank=False, null=False)
    photo = models.ImageField(null=True, blank=False)
