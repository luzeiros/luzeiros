from django.contrib import admin
from luzeiros.radio.models.program import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'presenter', 'created_at', 'updated_at']

    # Ensure applications cannot write in admin site
    def has_add_permission(self, request):
        return not request.user.is_app or not request.user.is_active

    def has_change_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active

    def has_delete_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active
