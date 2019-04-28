from django.contrib import admin
from luzeiros.radio.models.presenter import Presenter
from luzeiros.radio.admin.inlines.program import ProgramInline


@admin.register(Presenter)
class PresenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'programs_count', 'updated_at']
    inlines = [ProgramInline]

    # Ensure applications cannot write in admin site
    def has_add_permission(self, request):
        return not request.user.is_app or not request.user.is_active

    def has_change_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active

    def has_delete_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active
