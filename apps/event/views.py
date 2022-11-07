from rest_framework.viewsets import ModelViewSet
from apps.event.serializers import GroupSerializer, GameSerializer
from apps.event.models import Group, Game, Result
from django_filters.rest_framework import DjangoFilterBackend
from apps.event.filters import GameFilter


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    http_method_names = ['get', 'head', 'options']


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all().order_by('-time')
    serializer_class = GameSerializer
    http_method_names = ['get', 'head', 'options']
    filter_backends = [DjangoFilterBackend]
    filterset_class = GameFilter