from django.contrib import admin
from apps.zakovat.models import Team, Member

admin.site.register(Member)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'created_at')
    list_filter = ('name', 'leader', 'created_at')
    search_fields = ('name', 'leader', 'created_at')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('name',)}


