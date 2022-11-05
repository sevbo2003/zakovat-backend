from rest_framework.viewsets import ModelViewSet
from apps.zakovat.models import Team
from apps.zakovat.serializers import TeamSerializer
from typing import List

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names: List[str] = ['get', 'head', 'options']
