from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from apps.extrapages.models import Developer, BestPlayer, BestPlayerInfo, CurrentGame, YouTubeLink
from apps.extrapages.serializers import DeveloperSerializer, BestPlayerSerializer, CurrentGameSerializer, YouTubeLinkSerializer
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
        queryset = BestPlayer.objects.all()
        serializer = BestPlayerSerializer(queryset, many=True)
        try:
            info = BestPlayerInfo.objects.all().first()
        except:
            info = "No info :)"
        return Response(
            {
                "description": info.description,
                "information": serializer.data
            }
        )


class CurrentGameViewSet(viewsets.ViewSet):
    queryset = CurrentGame.objects.all()
    serializer_class = CurrentGameSerializer
    http_method_names = ['get', 'head', 'options']

    def list(self, request):
        object = self.queryset.last()
        serializer = CurrentGameSerializer(object)
        return Response(serializer.data, status=HTTP_200_OK)


class YouTubeLinkViewSet(viewsets.ViewSet):
    queryset = YouTubeLink.objects.all()
    serializer_class = YouTubeLinkSerializer
    http_method_names = ['get', 'head', 'options']

    def list(self, request):
        serializer = YouTubeLinkSerializer(self.queryset.last())
        return Response(serializer.data, status=HTTP_200_OK)