from rest_framework import serializers
from ...models import Faculty as FacultyModel


class Faculty(serializers.ModelSerializer):
    class Meta:
        model = FacultyModel
        fields = '__all__'