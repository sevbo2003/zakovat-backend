from django.contrib import admin
from apps.event.models import Group, Game


class GameInline(admin.TabularInline):
    model = Game
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    inlines = [GameInline]


admin.site.register(Group, GroupAdmin)
admin.site.register(Game)
