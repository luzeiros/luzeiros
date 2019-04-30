# Specifying upload paths


def path_for_track(instance, filename):
    """
    Upload to: music/artist_300/album_1/tracks/<filename>
    """
    artist = instance.artist.id
    album = instance.album.id
    return f'music/artist_{artist}/album_{album}/tracks/'


def path_for_album(instance, filename):
    """
    Upload to: music/artist_300/album_1/<filename>
    """
    artist = instance.artist.id
    return f'music/artist_{artist}/album_{album}/'


def path_for_artist(instance, filename):
    """
    Upload to: music/artist_300/<filename>
    """
    artist = instance.artist.id
    return f'music/artist_{artist}/'
