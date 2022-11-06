from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from apps.zakovat.views import TeamViewSet, MemberViewSet
from apps.event.views import GroupViewSet

router = DefaultRouter()
router.register('teams', TeamViewSet)
router.register('members', MemberViewSet)
router.register('groups', GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)