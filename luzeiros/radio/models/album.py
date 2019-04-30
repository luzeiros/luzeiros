from django.db import models
from .helpers.identifier import make_identifier
from .helpers.music import path_for_album
from .artist import Artist


class Album(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    artwork = models.ImageField(blank=True, upload_to=path_for_album)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    release_date = models.DateField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'radio_albums'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    @property
    def tracks_count(self):
        return self.tracks.count()

    def __str__(self):
        return self.title
