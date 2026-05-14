from django.contrib import admin

from .models import Role, UserRole


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("code", "name", "description")


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "company", "is_active", "granted_at")
    list_filter = ("role", "is_active")
    search_fields = ("user__username", "user__email", "company__name")
    autocomplete_fields = ("user", "role", "company")
    readonly_fields = ("granted_at",)

