from rest_framework import serializers
from ...models import Classroom as ClassroomModel
from .Housing import Housing as HousingSerializer
from .ClassroomType import ClassroomType as ClassroomTypeSerializer


class Classroom(serializers.ModelSerializer):
    housing = HousingSerializer(many=True)
    classroom_type = ClassroomTypeSerializer(many=True)
    class Meta:
        model = ClassroomModel
        fields = '__all__'