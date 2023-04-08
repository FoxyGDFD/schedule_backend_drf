from rest_framework import serializers
from ...models import ClassroomType as ClassroomTypeModel



class ClassroomType(serializers.ModelSerializer):
    class Meta:
        model = ClassroomTypeModel
        fields = '__all__'