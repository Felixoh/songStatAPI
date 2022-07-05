import csv
from django.utils import timezone
from spotAPI.models import Track,Playlist,Album,Artist,Image
from django.db.utils import IntegrityError

def save_track_albums():
    with open("assets/track_albums.csv","r") as csv_file:
        data = csv.reader(csv_file,delimiter=",")
        track_albums = {t_alb.trackID : t_alb for t_alb in Album.objects.all()}

        track_albs = []
        for row in data:
            track_SpotID = row[1]
            track_ID  = track_albums.get(track_SpotID)
            if not track_ID:
                track_ID = Album.objects.create(trackID=row[1])
                track_albums[track_ID.track_ID] = track_ID
            track_alb = Album(
                track_ID=row[1]
            )
            track_albs.append(track_alb)
            if len(track_albs) > 5000:
                Album.objects.bulk_create(track_albs)

        if track_albs:
            Album.objects.create(track_albs)

def save_track_info():
    '''
    Template tasks for saving all information related to all tracks that will be stored
    in our databases for later usage:
    '''

    with open("assets/tracks_info.csv","r",encoding="utf8") as csv_file:
        data = csv.reader(csv_file,delimiter=",")
        track_albums = {t_alb.track_SpotID : t_alb for t_alb in Track.objects.all()}

        for row in data:
            try:
                track_SpotID = row[1]
                track_Number = row[2]
                track_type = row[3]
                track_popular = row[4]
                track_name = row[5]
                track_duration = row[6]
                track_ID  = track_albums.get(track_SpotID)
                
                track_albs = []
                if not track_ID:
                    track_ID = Track.objects.create(
                        track_SpotID=track_SpotID,
                        track_Name = track_name,
                        track_No = track_Number,
                        track_Type = track_type,
                        track_Popularity = track_popular,
                        track_duration= track_duration
                        )

                    track_albums[track_ID.track_SpotID] = track_ID

                track_alb = Track(
                    track_Name = track_name,
                    track_SpotID = track_SpotID,
                    track_No = track_Number,
                    track_Type = track_type,
                    track_Popularity = track_popular,
                    track_duration= track_duration
                )

                track_albs.append(track_alb)

                if len(track_albs) > 5000:
                    try:
                        Track.objects.bulk_create(track_albs)
                        track_albs = []
                    except IntegrityError:
                        continue

                if track_albs:
                    Track.objects.create(track_albs)   
            except:
                continue

def save_artistInfo():
    '''
    Template for information about an artist and all related data to be stored in database:
    @testing phase ...

    '''
    with open("assets/artistinfo_csv.csv","r",encoding="utf8") as csv_file:
        data = csv.reader(csv_file,delimiter=",")
        artists = {art.art_SpotID : art for art in Artist.objects.all()}

        for row in data:
            try:
                art_name = row[1]
                art_id = row[2]
                art_follower = row[3]
                art_popularity = row[4]
                art_type = row[5]
                art_uri = row[6]
                art_href = row[7]

                art_ID  = artists.get(art_id)
                artist_dt = []
                if not art_ID:
                    art_ID = Artist.objects.create(
                        art_SpotID= art_id,
                        art_Name = art_name,
                        art_popularity = art_popularity,
                        art_URI = art_uri,
                        art_type = art_type,
                        art_HREF = art_href,
                        art_followers = art_follower,
                    )
                    artists[art_ID.art_SpotID] = art_ID

                artists[art_ID.art_SpotID] = art_ID
                art_info = Artist(
                    art_SpotID= art_id,
                    art_Name = art_name,
                    art_popularity = art_popularity,
                    art_URI = art_uri,
                    art_type = art_type,
                    art_HREF = art_href,
                    art_followers = art_follower,
                )

                artist_dt.append(art_info)
                if len(artist_dt) > 5000:
                    try:
                        Artist.objects.bulk_create(artist_dt)
                        artist_dt = []
                    except IntegrityError:
                        continue
                if artist_dt:
                    Artist.objects.create(artist_dt)
            except:
                continue

def save_playlistInfo():
    '''
    Save all data and information related to an playlist in system:
    '''
    with open("assets/playlist_data.csv","r",encoding="utf8") as csv_file:
        data = csv.reader(csv_file,delimiter=",")
        playlists = {art.play_SpotID : art for art in Playlist.objects.all()}

        for row in data:
            try:
                play_name = row[1]
                play_id = row[5]
                play_Href = row[4]
                play_Descrition = row[3]
                play_collabs = row[2]
                play_types = row[6]
                play_total_tracks = row[7]

                play_ID  = playlists.get(play_id)
                artist_dt = []
                if not play_ID:
                    play_ID = Playlist.objects.create(
                      play_SpotID = play_id,
                      play_Name = play_name,
                      play_Href = play_Href,
                      play_Descrition = play_Descrition,
                      play_collabs = play_collabs,
                      play_types = play_types,
                      play_total_tracks = play_total_tracks
                    )
                    playlists[play_ID.play_SpotID] = play_ID

                play_info = Playlist(
                      play_SpotID = play_id,
                      play_Name = play_name,
                      play_Href = play_Href,
                      play_Descrition = play_Descrition,
                      play_collabs = play_collabs,
                      play_types = play_types,
                      play_total_tracks = play_total_tracks
                )
                
                artist_dt.append(play_info)
                if len(artist_dt) > 5000:
                    try:
                        Playlist.objects.bulk_create(artist_dt)
                        artist_dt = []
                    except IntegrityError:
                        continue
                if artist_dt:
                    Playlist.objects.create(artist_dt)
            except:
                continue

def save_albumInfo():
    pass

def save_trackAlb_fk():
    '''
    This is a foreign key table that must ensure all fields are correctly inserted in the database systems.
    '''
    with open("assets/track_albums.csv","r",encoding="utf8") as csv_file:
        data = csv.reader(csv_file,delimiter=",")
        # track_albums = {t_alb.trackID : t_alb for t_alb in Album.objects.all()}
        for row in data:
            try:
                track_SpotID = row[1]
                # track_ID  = track_albums.get(track_SpotID)
                track_albs = []
                track_ID = Album.objects.create(track_SpotID=track_SpotID)
                # track_albums[track_ID.track_SpotID] = track_ID
                track_alb = Album(trackID=track_SpotID)
                track_albs.append(track_alb)

                if len(track_albs) > 5000:
                    try:
                        Album.objects.bulk_create(track_albs)
                        track_albs = []
                    except IntegrityError:
                        continue
                if track_albs:
                    Album.objects.create(track_albs)
            except:
                continue

