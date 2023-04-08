from rest_framework import serializers
from ...models import LessonNumber as LessonNumberModel


class LessonNumber(serializers.ModelSerializer):
    class Meta:
        model = LessonNumberModel
        fields = '__all__'