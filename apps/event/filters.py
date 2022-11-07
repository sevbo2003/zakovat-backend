from apps.event.models import Game, Result
import django_filters


class GameFilter(django_filters.FilterSet):
    group = django_filters.CharFilter(field_name='group__name')
    class Meta:
        model = Game
        fields = ['group', 'team1', 'team2','is_finished']