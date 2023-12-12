from rest_framework import serializers
from ...models import Classroom as ClassroomModel


class Classroom(serializers.ModelSerializer):
    class Meta:
        model = ClassroomModel
        fields = '__all__'