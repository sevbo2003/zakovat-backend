from rest_framework import serializers
from apps.zakovat.serializers import TeamSerializer
from apps.event.models import Group, Game, Result
from django.db.models import Q, F, Sum, Count, Case, When, IntegerField, Value, CharField, OuterRef, Subquery, Max, Min


class GroupSerializer(serializers.ModelSerializer):
    teams = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = ['name', 'teams']
    
    def get_teams(self, obj):
        teams = {}
        for i in obj.teams.all():
            try:
                x = Result.objects.filter(winner=i).annotate(score=Sum("score1")).values('score').first()['score']
            except:
                x = 0
            try:
                y = Result.objects.filter(loser=i).annotate(score=Sum("score2")).values('score').first()['score']
            except:
                y = 0
            teams[i.name] = [Game.objects.filter(Q(team1=i) | Q(team2=i)).count(), x + y]
        return teams


class GameSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField()
    team1 = serializers.StringRelatedField(source='team1.name')
    team2 = serializers.StringRelatedField(source='team2.name')
    class Meta:
        model = Game
        fields = ['group', 'team1', 'team2', 'time', 'is_finished']


class ResultSerializer(serializers.ModelSerializer):
    game = serializers.StringRelatedField()
    winner = serializers.StringRelatedField(source='winner.name')
    loser = serializers.StringRelatedField(source='loser.name')
    class Meta:
        model = Result
        fields = ['game', 'winner', 'loser', 'score1', 'score2']