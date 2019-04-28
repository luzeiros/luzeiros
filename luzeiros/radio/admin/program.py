from django.contrib import admin
from luzeiros.radio.models.program import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass
