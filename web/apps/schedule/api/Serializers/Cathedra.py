from rest_framework import serializers
from ...models import Cathedra as CathedraModel


class Cathedra(serializers.ModelSerializer):
    class Meta:
        model = CathedraModel
        fields = '__all__'