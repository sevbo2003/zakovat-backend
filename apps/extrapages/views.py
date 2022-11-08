from rest_framework.viewsets import ModelViewSet
from apps.extrapages.models import Developer
from apps.extrapages.serializers import DeveloperSerializer


class DeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    http_method_names = ['get', 'head', 'options']