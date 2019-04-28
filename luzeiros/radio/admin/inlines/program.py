from django.contrib import admin
from luzeiros.radio.models.program import Program


class ProgramInline(admin.StackedInline):
    model = Program
    extra = 1
