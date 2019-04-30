from django.db import models
from .helpers.identifier import make_identifier
from .helpers.music import path_for_track
from .album import Album
from .artist import Artist


class Track(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    title = models.CharField(blank=True, max_length=30)
    duration = models.IntegerField(blank=True)
    artist = models.ForeignKey(Artist, related_name='tracks', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    preview_file = models.FileField(blank=True, upload_to=path_for_track)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'radio_tracks'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    @property
    def related_tracks_by_artist(self):
        return self.artist.tracks.all()

    @property
    def related_tracks_by_album(self):
        return self.album.tracks.all()

    @property
    def has_preview(self):
        return self.preview_file is not None

    def __str__(self):
        return self.title
