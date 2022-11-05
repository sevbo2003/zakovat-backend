from rest_framework import serializers
from apps.zakovat.models import Team


class TeamSerializer(serializers.ModelSerializer):
    leader = serializers.StringRelatedField()
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'leader', 'members', 'image', 'description']