from rest_framework import serializers
from ...models import Direction as DirectionModel


class Direction(serializers.ModelSerializer):
    class Meta:
        model = DirectionModel
        fields = '__all__'