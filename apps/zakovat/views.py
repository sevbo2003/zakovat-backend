from rest_framework.viewsets import ModelViewSet
from apps.zakovat.models import Team, Member
from apps.zakovat.serializers import TeamSerializer, MemberSerializer
from apps.event.serializers import ResultSerializer
from apps.event.models import Result
from typing import List
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status



class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names: List[str] = ['get', 'head', 'options']
    lookup_field = 'slug'

    @action(detail=True, methods=['get'], url_name='past-results')
    def nim_chorak_results(self, request, slug=None):
        team = self.get_object()
        query = team.result_set.all() | team.loser.all() | Result.objects.filter(draw=True, game__team1=team) | Result.objects.filter(draw=True, game__team2=team)
        query = query.order_by("game__time")
        serializer = ResultSerializer(query, many=True)
        return Response({
            "team": {
                "id": team.id,
                "name": team.name
            },
            "results": serializer.data
            }, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def wins(self, request, slug=None):
        team = self.get_object()
        results = team.result_set.all()
        serializer = ResultSerializer(results, many=True)
        return Response({
            "team": {
                "id": team.id,
                "name": team.name
            },
            "results": serializer.data
            }, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def loses(self, request, slug=None):
        team = self.get_object()
        results = team.loser.all()
        serializer = ResultSerializer(results, many=True)
        return Response({
            "team": {
                "id": team.id,
                "name": team.name
            },
            "results": serializer.data
            }, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def draws(self, request, slug=None):
        team = self.get_object()
        results = Result.objects.filter(draw=True, game__team1=team) | Result.objects.filter(draw=True, game__team2=team)
        serializer = ResultSerializer(results, many=True)
        return Response({
            "team": {
                "id": team.id,
                "name": team.name
            },
            "results": serializer.data
            }, status=status.HTTP_200_OK)

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    http_method_names: List[str] = ['get', 'head', 'options']
