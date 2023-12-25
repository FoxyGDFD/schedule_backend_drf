from rest_framework import serializers
from ...models import Exam as ExamModel
from .Subject import Subject
from .Classroom import Classroom
from .Teacher import Teacher
from .Group import Group

class Exam(serializers.ModelSerializer):
    subject = Subject(read_only=True)
    classroom = Classroom(read_only=True)
    teacher = Teacher(read_only=True, many=True)
    group = Group(read_only=True, many=True)
    
    class Meta:
        model = ExamModel
        fields = '__all__'