from django.contrib import admin
from apps.event.models import Group, Game, Result
from apps.extrapages.models import CurrentGame


class GameInline(admin.TabularInline):
    model = Game
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    inlines = [GameInline]


admin.site.register(Group, GroupAdmin)
admin.site.register(Game)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('game', 'winner', 'score1', 'score2')


@admin.register(CurrentGame)
class CurrentGameAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'score1', 'score2')
    