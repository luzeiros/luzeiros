from django.contrib import admin
from luzeiros.radio.models.presenter import Presenter


class PresenterInline(admin.ModelAdmin):
    model = Presenter
    extra = 1
