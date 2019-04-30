from django.contrib import admin
from luzeiros.radio.models.artist import Artist
from luzeiros.radio.admin.inlines import AlbumInline
from luzeiros.radio.admin.inlines import TrackInline


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline, TrackInline]
    list_display = ['id', 'name', 'albums_count']
