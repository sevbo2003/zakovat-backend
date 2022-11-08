from django.contrib import admin
from apps.extrapages.models import Developer
from typing import Sequence


@admin.register(Developer)
class AdminDeveloper(admin.ModelAdmin):
    list_display = ['name', 'group', 'role']
    search_fields: Sequence[str] = ['name', 'group', 'role']