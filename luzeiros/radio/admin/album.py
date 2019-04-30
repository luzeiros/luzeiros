from django.contrib import admin
from ..models.album import Album
from .inlines import TrackInline


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInline]
    list_display = ['title', 'artist', 'tracks_count', 'release_date']
    list_editable = ['release_date']
