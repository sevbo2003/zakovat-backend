from rest_framework.viewsets import ModelViewSet
from apps.event.serializers import GroupSerializer, GameSerializer
from apps.event.models import Group, Game, Result


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    http_method_names = ['get', 'head', 'options']


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all().order_by('-time')
    serializer_class = GameSerializer
    http_method_names = ['get', 'head', 'options']