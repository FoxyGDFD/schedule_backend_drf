from rest_framework import serializers
from ...models import Lesson as LessonModel
from .LessonNumber import LessonNumber
from .Subject import Subject
from .Classroom import Classroom
from .LessonType import LessonType
from .Teacher import Teacher
from .Group import Group
class Lesson(serializers.ModelSerializer):
    
    number = LessonNumber(read_only=True)
    subject = Subject(read_only=True)
    classroom = Classroom(read_only=True)
    lesson_type = LessonType(read_only=True)
    teacher = Teacher(read_only=True, many=True)
    group = Group(read_only=True, many=True)

    class Meta:
        model = LessonModel
        fields = '__all__'