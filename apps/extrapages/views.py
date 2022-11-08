from rest_framework.viewsets import ModelViewSet
from apps.extrapages.models import Developer, BestPlayer
from apps.extrapages.serializers import DeveloperSerializer, BestPlayerSerializer


class DeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    http_method_names = ['get', 'head', 'options']


class BestPlayerViewSet(ModelViewSet):
    queryset = BestPlayer.objects.all()
    serializer_class = BestPlayerSerializer
    http_method_names = ['get', 'head', 'options']