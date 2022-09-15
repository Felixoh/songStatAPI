from .dto import Dto
from concurrent.futures import ThreadPoolExecutor,as_completed
from .search import Search

class Concurrent(Search):
    '''
    Wrapper for all concurrent functions to be written Here that will fetch data from 
    the multiple sources of code in the functionalities that will be used to scrape 
    all expected data from the sites determined by the system Scrapers.
    '''
    
    def __init__(self,workers=20):
        self.workers = workers

    def fetch_ids(self):
        dto_obj = Dto()
        keywords = dto_obj.read_playlist_keyword()
        with ThreadPoolExecutor(self.workers) as executor:
            results = [executor.submit(dto_obj.write_playlist_ids,keyword) for keyword in keywords]
            for res in results:
                if res.done:
                    pass
                if res.exception:
                    pass

    def fetch_playlist_images(self):
        dto_obj = Dto()
        plays = dto_obj.read_playlist_keyword()
        play_ids = plays
        n_workers = self.workers
        chunksize = round(len(play_ids) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operation of workers into chunks to fetch data::
            for i in range(0,len(play_ids),chunksize):
                playlist_ids = play_ids[i:(i+chunksize)]
                result = [executor.submit(dto_obj.writeto_playlist_images,id) for id in playlist_ids]
                for res in result:
                    if res.done:
                        pass 
                    if res.exception:
                        pass

    def fetch_playlists(self):
        dto_obj = Dto()
        plays = dto_obj.read_playlist_keyword()
        play_ids = plays
        n_workers = self.workers

        chunksize = round(len(play_ids) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operation of workers into chunks to fetch concurrently data from Spotify.
            for i in range(0,len(play_ids),chunksize):
                playlist_ids = play_ids[i:(i+chunksize)]
                result = [executor.submit(dto_obj.writeto_playlist_data,id) for id in playlist_ids]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass

    def fetch_playlist_owners(self):
        pass

    def fetch_trackIDS(self):
        dto_obj = Dto()
        plays = dto_obj.read_playlist_ids()
        play_ids = plays
        n_workers = self.workers
        chunksize = round(len(play_ids) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operation of workers into chunks to fetch data::
            for i in range(0,len(play_ids),chunksize):
                playlist_ids = play_ids[i:(i+chunksize)]
                result = [executor.submit(dto_obj.write_playlist_tracks,id) for id in playlist_ids]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass

    def fetch_track_artists(self):
        artists = Dto().read_playlist_keyword()
        artist_list = artists[:500]
        n_workers = self.workers
        chunk_size = round(len(artist_list) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operations to chunks and fetch data:
            for i in range(0,len(artist_list),chunk_size):
                arti_list = artist_list[i:(i+chunk_size)]
                result = [executor.submit(Dto().writeto_trackArtists,art) for art in arti_list]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass

    def fetch_track_albums(self):
        artists = Dto().read_artist_names()
        artist_list = artists[:50]
        n_workers = self.workers
        chunk_size = round(len(artist_list) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operations to chunks and fetch data:
            for i in range(0,len(artist_list),chunk_size):
                arti_list = artist_list[i:(i+chunk_size)]
                result = [executor.submit(Dto().writeto_trackAlb,art) for art in arti_list]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass

    def fetch_trackInfo(self):
        artists = Dto().read_artist_names()
        artist_list = artists[:500]
        n_workers = self.workers
        chunk_size = round(len(artist_list) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operations to chunks and fetch data:
            for i in range(0,len(artist_list),chunk_size):
                arti_list = artist_list[i:(i+chunk_size)]
                result = [executor.submit(Dto().writeto_trackinfo,art) for art in arti_list]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass

    def fetch_artist_info(self):
        artists = Dto().read_artist_names()
        artist_list = artists[:500]
        n_workers = self.workers
        chunk_size = round(len(artist_list) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operations to chunks and fetch data:
            for i in range(0,len(artist_list),chunk_size):
                arti_list = artist_list[i:(i+chunk_size)]
                result = [executor.submit(Dto().writeto_artistInfo,art) for art in arti_list]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass

    def fetch_artist_images(self):
        artists = Dto().read_artist_names()
        artist_list = artists[:500]
        n_workers = self.workers
        chunk_size = round(len(artist_list) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operations to chunks and fetch data:
            for i in range(0,len(artist_list),chunk_size):
                arti_list = artist_list[i:(i+chunk_size)]
                result = [executor.submit(Dto().writeto_artist_Images,art) for art in arti_list]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass

    def fetch_artist_genres(self):
        """
        Not yet Implemented yet:
        """
        pass

    def fetch_albums(self):
        artists = Dto().read_artist_names()
        artist_list = artists
        n_workers = self.workers
        chunk_size = round(len(artist_list) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operations to chunks:
            for i in range(0,len(artist_list),chunk_size):
                arti_list = artist_list[i:(i+chunk_size)]
                result = [executor.submit(Dto().writeto_album_data,art) for art in arti_list]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass

    def fetch_albumImages(self):
        artists = Dto().read_artist_names()
        artist_list = artists
        n_workers = self.workers
        chunk_size = round(len(artist_list) / n_workers)
        with ThreadPoolExecutor(n_workers) as executor:
            #split the operations to chunks:
            for i in range(0,len(artist_list),chunk_size):
                arti_list = artist_list[i:(i+chunk_size)]
                result = [executor.submit(Dto().writeto_album_Images,art) for art in arti_list]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass
                        
    def fetch_albumArtists(self):
        artists = Dto().read_artist_names()
        artist_list = artists
        n_workers = self.workers
        chunk_size = round(len(artist_list) / n_workers)

        with ThreadPoolExecutor(n_workers) as executor:
            #split the operations to chunks :
            for i in range(0,len(artist_list),chunk_size):
                arti_list = artist_list[i:(i+chunk_size)]
                result = [executor.submit(Dto().writeto_album_artists,art) for art in arti_list]
                for res in result:
                    if res.done:
                        pass
                    if res.exception:
                        pass