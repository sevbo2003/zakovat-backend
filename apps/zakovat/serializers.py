from rest_framework import serializers
from apps.zakovat.models import Team, Member


class TeamSerializer(serializers.ModelSerializer):
    leader = serializers.StringRelatedField()
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'leader', 'members', 'image', 'description', 'slug']


class MemberSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ['full_name', 'team']
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    def get_team(self, obj):
        return obj.teams.values_list('name', flat=True)