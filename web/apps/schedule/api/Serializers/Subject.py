from rest_framework import serializers
from ...models import Subject as SubjectModel


class Subject(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = '__all__'