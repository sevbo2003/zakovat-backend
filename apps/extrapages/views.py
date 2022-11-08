from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import viewsets
from apps.extrapages.models import Developer, BestPlayer, BestPlayerInfo
from apps.extrapages.serializers import DeveloperSerializer, BestPlayerSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class DeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    http_method_names = ['get', 'head', 'options']


class BestPlayerViewSet(viewsets.ViewSet):
    queryset = BestPlayer.objects.all()
    serializer_class = BestPlayerSerializer
    http_method_names = ['get', 'head', 'options']

    def list(self, request):
        serializer = BestPlayerSerializer(self.queryset, many=True)
        try:
            info = BestPlayerInfo.objects.all().first()
        except:
            info = "No info :)"
        return Response(
            {
                "description": info.description,
                "info": serializer.data
            }
        )