
import spotipy
from  . import config
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

def search_all(query,limit=50,offset=0):
    client_credentials_manager = SpotifyClientCredentials(config.CLIENT_ID,config.CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    data = sp.search(query,limit,offset)
    keys = ["track","artists","albums","playlists"]
    items = data['tracks']['items']
    return items

class Search:
    """
    Python class wrapper for all API search functionalities for this scraper module 
    Search has the following methods:
    1. tracks
    2. playlist
    3. artist
    4. album
    5. get track ids from music
    6. get track data from track music playeds here :
    """

    client_credentials_manager = SpotifyClientCredentials(config.CLIENT_ID,config.CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    # ensures the result from single query does not exceed 1000 per query set by the query Limit Argument

    def __init__(self,query='',limit=50,offset=0,query_limit=1000):
        self.query = query
        self.limit = limit
        self.offset = offset
        self.query_limit = query_limit
    
    def search_all(self,query):
        data = self.sp.search(query,self.limit)
        return data

    def search_track_albums(self,query):
        track_SpotID = []
        track_album_name = []
        track_album_type = []
        track_albumSpotid = []
        track_album_release_date = []
        track_album_total_tracks = []
        track_album_release_date_precision = []
        track_alb_Uri = []
        track_alb_type = []

        numbers =[x for x in range(self.query_limit) if (x % 50 == 0)]
        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="track")
                tracks = data['tracks']['items']
                for t in tracks:
                    track_SpotID.append(t['id'])
                    track_album_type.append(t['album']['album_type'])
                    track_albumSpotid.append(t['album']['id'])
                    track_album_name.append(t['album']['name'])
                    track_album_release_date.append(t['album']['release_date'])
                    track_album_release_date_precision.append(t['album']['release_date_precision'])
                    track_album_total_tracks.append(t['album']['total_tracks'])
                    track_alb_Uri.append(t['album']['uri'])
                    track_alb_type.append(t['album']['type'])
            except:
                continue

        df1 = pd.DataFrame(track_SpotID)

        df2 = pd.DataFrame(track_album_name)
        df3 = pd.DataFrame(track_album_type)
        df4 = pd.DataFrame(track_albumSpotid)
        df5 = pd.DataFrame(track_album_release_date)
        df6 = pd.DataFrame(track_album_total_tracks)
        df7 = pd.DataFrame(track_album_release_date_precision)
        df8 = pd.DataFrame(track_alb_type)

        track_alb_InfoDF = pd.concat([df1],axis=1)

        return track_alb_InfoDF

    def search_track_artist(self,query):
        #artists informations
        track_SpotID = []
        track_art_URL = []
        track_alb_SpotID = []
        track_art_type = []
        track_artist_name = []
        track_artist_id = []
        track_artists_uri = []
        
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0)]
        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="track")
                tracks = data['tracks']['items']
                for d in tracks:
                    track_SpotID.append(d['id'])
                    track_art_URL.append(d['artists'][0]['external_urls']['spotify'])
                    track_artist_name.append(d['artists'][0]['name'])
                    track_artist_id.append(d['artists'][0]['id'])
                    track_alb_SpotID.append(d['album']['id'])
                    track_art_type.append(d['artists'][0]['type'])
                    track_artists_uri.append(d['artists'][0]['uri'])
            except:
                continue

        df1 = pd.DataFrame(track_SpotID)
        df2 = pd.DataFrame(track_art_URL)
        df3 = pd.DataFrame(track_alb_SpotID)
        df4 = pd.DataFrame(track_art_type)
        df5 = pd.DataFrame(track_artist_name)
        df6 = pd.DataFrame(track_artist_id)
        df7 = pd.DataFrame(track_artists_uri)
        
        track_artists_InfoDF = pd.concat([df1,df2,df3,df4,df5,df6,df7],axis=1)
        return track_artists_InfoDF

    def search_tracks(self,query):
        track_Spotid = []
        track_tracknumber = []
        track_track_type = []
        track_popularity = []
        track_name = []
        track_track_duration_ms = []
        
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0)]
        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="track")
                tracks = data['tracks']['items']
                for d in tracks:
                    track_name.append(d['name'])
                    track_Spotid.append(d['id'])
                    # track_album.append(d['album'])
                    track_popularity.append(d['popularity'])
                    track_tracknumber.append(d['track_number'])
                    track_track_type.append(d['type'])
                    track_track_duration_ms.append(d['duration_ms'])
            except:
                continue

        df1 = pd.DataFrame(track_Spotid) 
        df2 = pd.DataFrame(track_tracknumber)
        df3 = pd.DataFrame(track_track_type)
        df4 = pd.DataFrame(track_popularity)
        df5 = pd.DataFrame(track_name)
        df6 = pd.DataFrame(track_track_duration_ms)
        trackInfoDF = pd.concat([df1,df2,df3,df4,df5,df6],axis=1)
        return trackInfoDF

    def search_playlist_images(self,query):
        """
        Returns data related to a playlist ID images in store and collection
        """
        playlist_ids = []
        playlist_images_heights = []
        playlist_images_urls = []
        playlist_images_widths = []
        
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0) ]
        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="playlist")
                playlists = data['playlists']['items']

                for d in playlists:
                    #playlist_images
                    playlist_images = d['images'] #all related image metadata from the data points of the playlist:
                    playlist_images_height = d['images'][0]['height'] #all related image metadata height
                    playlist_images_heights.append(playlist_images_height)

                    playlist_images_url = d['images'][0]['url'] #all related image  url
                    playlist_images_urls.append(playlist_images_url)
                    
                    playlist_images_width = d['images'][0]['width'] #all image related widths and their proportionality:
                    playlist_images_widths.append(playlist_images_width)

                    #playlist_id
                    playlist_id = d['id']
                    playlist_ids.append(playlist_id)

            except:
                continue

        df1 = pd.DataFrame(playlist_ids)
        df2 = pd.DataFrame(playlist_images_heights)
        df3 = pd.DataFrame(playlist_images_urls)
        df4 = pd.DataFrame(playlist_images_widths)

        playlist_imgesDF = pd.concat([df1,df2,df3,df4],axis=1)
        return playlist_imgesDF

    def search_playlist(self,query):
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0) ]
        playlist_tracks_urls_links = []
        playlist_total_tracks = []
        #data point 1
        playlist_data_tracks = {
            'playlist_url': playlist_tracks_urls_links,
            'playlist_total_tracks': playlist_total_tracks
        }

        playlist_owners_name = []
        playlist_owners_href = []
        playlist_owners_id = []
        playlist_owners_type = []
        playlist_owners_uri = []
        
        #data point 3:
        playlist_owners = {
            'playlist_owners_name':playlist_owners_name,
            'playlist_owners_href':playlist_owners_href,
            'playlist_owners_id':playlist_owners_id,
            'playlist_owners_type':playlist_owners_type,
            'playlist_owners_uri':playlist_owners_uri
        }

        playlist_names = []
        playlist_collabs = []
        playlist_descriptions = []
        playlist_hrefs = []
        playlist_ids = []
        playlist_types = []
        playlist_uris = []

        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="playlist")
                playlists = data['playlists']['items']
                #data point 4
                for d in playlists:
                    playlist_urls = d['tracks'] #general playlist href and total tracks contained in the playlist:
                    playlist_tracks_urls_links.append(d['tracks']['href'])
                    playlist_total_tracks.append(d['tracks']['total'])

                    #all playlist names from result:
                    playlist_name = d['name']
                    playlist_names.append(playlist_name)
                    
                    #playlist_collaborative
                    playlist_collab = d['collaborative']
                    playlist_collabs.append(playlist_collab)
                    
                    #playlist_description
                    playlist_description = d['description']
                    playlist_descriptions.append(playlist_description)
                    
                    #playlist_href 
                    playlist_href = d['href']
                    playlist_hrefs.append(playlist_href)
                    
                    #playlist_id
                    playlist_id = d['id']
                    playlist_ids.append(playlist_id)

                    #playlist_owner
                    playlist_owner = d['owner'] #collected related metadata about the owner of the music playlist :
                    playlist_owner_name = d['owner']['display_name']
                    playlist_owners_name.append(playlist_owner_name)
                    playlist_owner_href = d['owner']['href']
                    playlist_owners_href.append(playlist_owner_href)
                    playlist_owner_id = d['owner']['id']
                    playlist_owners_id.append(playlist_owner_id)
                    playlist_owners_type = d['owner']['type']
                    playlist_owner_uri = d['owner']['uri']
                    playlist_owners_uri.append(playlist_owner_uri)
                    
                    #playlist_type (public or private)
                    playlist_type = d['type']
                    playlist_types.append(playlist_type)

                    #playlist_uri
                    playlist_uri = d['uri']
                    playlist_uris.append(playlist_uri)
            except:
                continue

        #now save the data to dataframe:
        df1 = pd.DataFrame(playlist_names)
        df2 = pd.DataFrame(playlist_collabs)
        df3 = pd.DataFrame(playlist_descriptions)
        df4 = pd.DataFrame(playlist_hrefs)
        df5 = pd.DataFrame(playlist_ids)
        df6 = pd.DataFrame(playlist_types)
        df7 = pd.DataFrame(playlist_total_tracks)

        playlist_dataDF = pd.concat([df1,df2,df3,df4,df5,df6,df7],axis=1)
        return playlist_dataDF

    def search_playlist_ids(self,query):
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0) ]
        playlist_ids = []
        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="playlist")
                playlists = data['playlists']['items']
                for play in playlists:
                    playlist_ids.append(play['id'])
            except:
                continue

        return playlist_ids

    def search_artist_images(self,query):
        #Loop over 1500 > links of the artist images url and retrieve data
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0) ]
        #other enlisted data to 
        artist_id = []
        # artist_genres = []
        art_image_height = []
        art_image_width = []
        art_image_url = []

        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="artist")
                artists = data['artists']['items']
                for art in artists:
                    artist_id.append(art['id'])
                    art_image_height.append(art['images'][0]['height'])
                    art_image_width.append(art['images'][0]['width'])
                    art_image_url.append(art['images'][0]['url'])
                    # artist_genres.append(art['genres'])
            except:
                continue

        df1 = pd.DataFrame(artist_id)
        df2 = pd.DataFrame(art_image_height)
        df3 = pd.DataFrame(art_image_width)
        df4 = pd.DataFrame(art_image_url)
        artist_imageDF = pd.concat([df1,df2,df3,df4],axis=1)

        return artist_imageDF

    def search_artist_genres(self,query):
        #Loop over 1500 > links of the artist images url and retrieve data
        """
        Not yet implemented because of many to many Relationship existing 
        between an Artist and Genres of music Listened to :
        """
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0) ]
        #other enlisted data to 
        artist_id = []
        artist_genres = []
        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="artist")
                artists = data['artists']['items']
                for art in artists:
                    artist_id.append(art['id'])
                    artist_genres.append(art['genres'])
            except:
                continue
        df1 = pd.DataFrame(artist_id)
        df2 = pd.DataFrame(artist_genres)
        artist_genresDF = pd.concat([df1,df2],axis=1)
        return artist_genresDF

    def search_artist_info(self,query):
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0) ]
        artist_name = []
        artist_followers =[]
        artist_id =[]
        artist_popularity = []
        artist_type=[]
        artist_uri =[]
        artist_href =[]
        
        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="artist")
                artists = data['artists']['items']
                artist_total = data['artists']['total']

                for art in artists:
                    artist_name.append(art['name'])
                    artist_id.append(art['id'])
                    artist_followers.append(art['followers']['total'])
                    artist_popularity.append(art['popularity'])

                    artist_type.append(art['type'])
                    artist_uri.append(art['uri'])
                    artist_href.append(art['href'])

            except:
                continue

        df1 = pd.DataFrame(artist_name)
        df7 = pd.DataFrame(artist_id)
        df2 = pd.DataFrame(artist_followers)
        df3 = pd.DataFrame(artist_popularity)
        df4 = pd.DataFrame(artist_type)
        df5 = pd.DataFrame(artist_uri)
        df6 = pd.DataFrame(artist_href)

        artist_infoDF = pd.concat([df1,df2,df3,df3,df4,df5,df6,df7],axis=1)

        return artist_infoDF

    def search_album_artists(self,query):
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0) ]
        alb_ID = []
        alb_art_ID = []
        alb_art_Name = []
        alb_art_Type = []
        alb_art_Uri = []
        alb_art_Href = []

        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="album")
                albums = data['albums']['items']
                for al in albums:
                    alb_ID.append(al['id'])
                    alb_art_ID.append(al['artists'][0]['id'])
                    alb_art_Name.append(al['artists'][0]['name'])
                    alb_art_Type.append(al['artists'][0]['type'])
                    alb_art_Uri.append(al['artists'][0]['uri'])
                    alb_art_Href.append(al['artists'][0]['href'])          
            except:
                continue
            
        df1 = pd.DataFrame(alb_ID)
        df2 = pd.DataFrame(alb_art_ID)
        df3 = pd.DataFrame(alb_art_Name)
        df4 = pd.DataFrame(alb_art_Type)
        df5 = pd.DataFrame(alb_art_Uri)
        df6 = pd.DataFrame(alb_art_Href)

        albArtistDf = pd.concat([df1,df2,df3,df4,df5,df6],axis=1)
        return albArtistDf

    def search_album_Images(self,query):
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0) ]
        alb_ID = []
        alb_img_height = []
        alb_img_width = []
        alb_img_url = []

        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="album")
                albums = data['albums']['items']
                for al in albums:
                    alb_ID.append(al['id'])
                    alb_img_height.append(al['images'][0]['height'])
                    alb_img_url.append(al['images'][0]['url'])
                    alb_img_width.append(al['images'][0]['width'])           
            except:
                continue
        df1 = pd.DataFrame(alb_ID)
        df2 = pd.DataFrame(alb_img_height)
        df3 = pd.DataFrame(alb_img_width)
        df4 = pd.DataFrame(alb_img_url)

        albImagesDf = pd.concat([df1,df2,df3,df4],axis=1)
        return albImagesDf

    def search_album(self,query):
        numbers =[x for x in range(self.query_limit) if (x % 50 == 0) ]
        #data points to be scraped and returned by the System at compilation:
        alb_album_type = []
        alb_href = []
        alb_name =[]
        alb_release_date = []
        alb_release_date_precision =[]
        alb_total_tracks = []
        alb_type = []
        alb_uri = []
        alb_ID = []

        for num in numbers:
            try:
                data = self.sp.search(query,self.limit,num,type="album")
                albums = data['albums']['items']
                for al in albums:
                    alb_album_type.append(al['album_type'])
                    alb_ID.append(al['id'])
                    alb_href.append(al['href'])
                    alb_name.append(al['name'])
                    alb_release_date.append(al['release_date'])
                    alb_release_date_precision.append(al['release_date_precision'])
                    alb_total_tracks.append(al['total_tracks'])
                    alb_type.append(al['type'])
                    alb_uri.append(al['uri'])
            except:
                continue
            
        df1 = pd.DataFrame(alb_album_type)
        df2 = pd.DataFrame(alb_href)
        df3 = pd.DataFrame(alb_name)
        df4 = pd.DataFrame(alb_release_date)
        df5 = pd.DataFrame(alb_release_date_precision)
        df6 = pd.DataFrame(alb_total_tracks)
        df7 = pd.DataFrame(alb_type)
        df8 = pd.DataFrame(alb_uri)
        df9 = pd.DataFrame(alb_ID)

        #album_info
        album_infoDF = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9],axis=1)

        return album_infoDF
        #worked on later under improved standards later:

    def get_track_ids(self,playlist_id):
        track_id_list = []
        playlist = self.sp.playlist(playlist_id)
        for item in playlist['tracks']['items']:
            music_track = item['track']
            track_id_list.append(music_track['id'])
        return track_id_list

    def get_track_albumData(self,track_id):
        meta = self.sp.track(track_id)

        df1 = pd.DataFrame({"track_albID":meta['album']['id']})
        df2 = pd.DataFrame({"track_albURI":meta['album']['uri']})
        df3 = pd.DataFrame({"track_albumName":meta['album']['name']})
        df4 = pd.DataFrame({"track_alb":meta['album']['release_date']})
        df5 = pd.DataFrame({"album":meta['album']['release_date_precision']})
        
        track_albumInfoDF = pd.concat([df1,df2,df3,df4,df5],axis=1)

        return track_albumInfoDF

    def get_track_data(self,track_id):
        meta = self.sp.track(track_id=track_id)

        df1 = pd.DataFrame({"track_spotID":meta['id']},index=[0])
        df2 = pd.DataFrame({"track_number":meta['track_number']},index=[0])
        df3 = pd.DataFrame({"track_type": meta['type']},index=[0])
        df4 = pd.DataFrame({"track_popularity":meta['popularity']},index=[0])
        df5 = pd.DataFrame({"track_duration":meta['duration_ms']},index=[0])
        df6 = pd.DataFrame({"track_disknumber":meta['disc_number']},index=[0])
        df7 = pd.DataFrame({"track_albID":meta['album']['id']},index=[0])
        
        track_dataDF = pd.concat([df1,df2,df3,df4,df5,df6,df7],axis=1)
        return track_dataDF