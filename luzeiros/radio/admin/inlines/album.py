from django.contrib import admin
from luzeiros.radio.models.album import Album


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1
