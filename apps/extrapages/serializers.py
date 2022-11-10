from rest_framework import serializers
from apps.extrapages.models import Developer, BestPlayer, CurrentGame, YouTubeLink


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'


class BestPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestPlayer
        fields = '__all__'


class CurrentGameSerializer(serializers.ModelSerializer):
    team1 = serializers.CharField(source='team1.name')
    team2 = serializers.CharField(source='team2.name')
    class Meta:
        model = CurrentGame
        fields = ['team1', 'team2', 'score1', 'score2']


class YouTubeLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeLink
        fields = '__all__'