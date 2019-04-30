from django.contrib import admin
from luzeiros.radio.models.track import Track


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'album', 'artist', 'has_preview']
