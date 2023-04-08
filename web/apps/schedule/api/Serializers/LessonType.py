from rest_framework import serializers
from ...models import LessonType as LessonTypeModel


class LessonType(serializers.ModelSerializer):
    class Meta:
        model = LessonTypeModel
        fields = '__all__'