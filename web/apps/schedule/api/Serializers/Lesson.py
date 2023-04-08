from rest_framework import serializers
from ...models import Lesson as LessonModel


class Lesson(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = '__all__'