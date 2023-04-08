from rest_framework import serializers
from ...models import Teacher as TeacherModel


class Teacher(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'