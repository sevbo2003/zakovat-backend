from rest_framework import serializers
from apps.extrapages.models import Developer, BestPlayer


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'


class BestPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestPlayer
        fields = '__all__'
        