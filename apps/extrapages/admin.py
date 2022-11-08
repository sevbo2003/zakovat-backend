from django.contrib import admin
from apps.extrapages.models import Developer, BestPlayer
from typing import Sequence


@admin.register(Developer)
class AdminDeveloper(admin.ModelAdmin):
    list_display = ['name', 'group', 'role']
    search_fields: Sequence[str] = ['name', 'group', 'role']


@admin.register(BestPlayer)
class AdminBestPlayer(admin.ModelAdmin):
    list_display = ['name', 'group', 'team']
    search_fields: Sequence[str] = ['name', 'group', 'team']