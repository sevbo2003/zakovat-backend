from apps.event.models import Game, Result
import django_filters


class GameFilter(django_filters.FilterSet):
    group = django_filters.CharFilter(field_name='group__name')
    class Meta:
        model = Game
        fields = ['group', 'team1', 'team2','is_finished']


class ResultFilter(django_filters.FilterSet):
    group = django_filters.CharFilter(field_name='game__group__name')
    game = django_filters.CharFilter(field_name='game__id')
    winner = django_filters.CharFilter(field_name='winner')
    loser = django_filters.CharFilter(field_name='loser')
    class Meta:
        model = Result
        fields = ['game', 'group', 'winner', 'loser']