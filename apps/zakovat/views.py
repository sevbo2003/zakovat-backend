from rest_framework.viewsets import ModelViewSet
from apps.zakovat.models import Team, Member
from apps.zakovat.serializers import TeamSerializer, MemberSerializer
from typing import List

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names: List[str] = ['get', 'head', 'options']


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    http_method_names: List[str] = ['get', 'head', 'options']
