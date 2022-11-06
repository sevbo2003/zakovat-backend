from rest_framework.viewsets import ModelViewSet
from apps.event.serializers import GroupSerializer
from apps.event.models import Group, Game, Result


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    http_method_names = ['get', 'head', 'options']