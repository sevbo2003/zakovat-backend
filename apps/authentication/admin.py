from django.contrib import admin
from apps.authentication.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


admin.site.unregister(Group)

class CustomUserAdmin(UserAdmin):
    list_display = ('email','username', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('email','username', 'first_name', 'last_name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'username', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','username', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
