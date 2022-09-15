from celery import shared_task
# from scraper.save_DB import save_artistDT

#initialise our scraper tasks with celery from this point:
from scraper.concurrent import Concurrent
conc = Concurrent()

# main tasks
# @shared_task
# def save_artistInfo(id,name):
#     save_artistDT(id,name)

# @shared_task
# def fetch_playlist():
#     Concurrent().fetch_playlists()

@shared_task
def fetch_artists():
    Concurrent(workers=20).fetch_artist_info() 

# end
# @shared_task
# def fetch_track_albums():
#     Concurrent().fetch_track_albums()

# @shared_task
# def fetch_track_artists():
#     Concurrent(workers=10).fetch_track_artists()

# @shared_task
# def fetch_track_info():
#     Concurrent(workers=10).fetch_trackInfo()


# @shared_task
# def fetch_artist_images():
#     Concurrent(workers=10).fetch_artist_images()
    
# @shared_task
# def fetch_playlists():
#     Concurrent(workers=10).fetch_playlists()

# @shared_task
# def fetch_playlist_images():
#     Concurrent(workers=10).fetch_playlist_images()

# @shared_task
# def fetch_albumsDT():
#     Concurrent(workers=10).fetch_albums()

# @shared_task
# def fetch_album_images():
#     Concurrent(workers=10).fetch_albumImages()

# @shared_task
# def fetch_albumArtists():
#     Concurrent(workers=10).fetch_albumArtists()

#Append below all data savig to database tasks to be run by our celery worker
#     