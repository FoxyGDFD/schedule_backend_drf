from rest_framework import serializers
from ...models import Exam as ExamModel


class Exam(serializers.ModelSerializer):
    class Meta:
        model = ExamModel
        fields = '__all__'