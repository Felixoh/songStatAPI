from email import header
from .search import Search 
import time 
from time import sleep
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from random import random
import os

class Dto:
    '''
    Data To Object(Dto) class does all functionality related to 
    1. Writing
    2. Reading
    3. Appending
    4. Serialization and data transformations.

    '''
    
    def __init__(self):
        pass

    def create_folder(self):
        try:
            curr = os.getcwd()
            newfold = os.mkdir("assets")
        except FileExistsError:
            print("Error reading files:")

    def write_playlist_ids(self,keyword):
        playlist_obj = Search()
        playlist_ids = playlist_obj.search_playlist_ids(keyword)

        try:
            with open("assets/playlist_ids.txt","a") as f:
                for playlist in playlist_ids:
                    f.write(playlist + "\n")
                    print("writing"+ playlist)

        except FileNotFoundError as err:
            print(err)

    def read_playlist_keyword(self):
        try:
            with open("assets/keywords.txt","r") as r:
                lines = r.readlines() 
                return lines
                
        except FileNotFoundError as err:
            print(err)

    def read_playlist_ids(self):
        with open("assets/playlist_ids.txt","r") as r:
            playlist_ids = r.readlines()
            return playlist_ids

    def read_artist_names(self):
        #rd = reader
        with open("assets/artist_names.txt","r") as rd:
            art_names = rd.readlines()
            return art_names

    def writeto_trackinfo(self,keyword):
        """
        Writer to save all data related to track into databases:
        """
        tracks_info = Search().search_tracks(keyword)
        try:
            tracks_info.to_csv("assets/tracks_info.csv",mode="a",header=False)
            print("Writing to file ....")
        except FileExistsError:
            print("Error writing to the file shown above:")

    def writeto_trackAlb(self,keyword):
        tracks_info = Search().search_track_albums(keyword)
        try:
            tracks_info.to_csv("assets/track_albums.csv",mode="a",header=False)
            print("Writing to file ....")
        except FileExistsError:
            pass

    def writeto_trackArtists(self,keyword):
        tracks_info = Search().search_track_artist(keyword)
        try:
            tracks_info.to_csv("assets/tracks_Artists.csv",mode="a",header=False)
            print("Writing to file ....")
        except FileExistsError:
            print("Error writing to the file shown above:")


    def writeto_artistInfo(self,keyword):
        """
        Write/Save all information related to an artist to db:
        """
        art_infos = Search().search_artist_info(keyword)
        try:
            art_infos.to_csv("assets/artistInfo_csv.csv",mode="a",header=False)
            print("Writing the Data to CSV now ......")
        except FileExistsError:
            print("The file allready exists please cannot save")

    def writeto_artist_Images(self,keyword):
        """
        Generate csv data to be saved to Related artist images DB

        """
        search_img = Search().search_artist_images(keyword)
        try:
            search_img.to_csv("assets/artist_images.csv",mode="a",header=False)
            print("writing images to CSV file")
        except FileExistsError:
            print("Error saving the file to databases:")
        except FileNotFoundError:
            print("File cannot be found in the system")

    def writeto_playlist_images(self,keyword):
        """
        Generate csv data for image data to be linked to a playlist image
        in table2
        """
        playlist_obj = Search()
        play_imges = playlist_obj.search_playlist_images(keyword)
        try:
            play_imges.to_csv("assets/playlist_images.csv",mode="a",header=False)
            print("Writiing to CSV now ...... ... ")
        except FileExistsError:
            print("Error the file is non existent please retry another time")
        except FileNotFoundError:
            print("The file cannot be found now please try again:")

    def writeto_playlist_data(self,keyword):
        playlist_obj = Search()
        playlist_data = playlist_obj.search_playlist(keyword)
        try:
            playlist_data.to_csv("assets/playlist_data.csv",mode="a",header=False)
            print("Writing Data ...")
        except FileNotFoundError:
            print("error the file is not found:")
    
    def writeto_album_data(self,keyword):
        alb_obj = Search()
        alb_data = alb_obj.search_album(keyword)
        try:
            alb_data.to_csv("assets/album_data.csv",mode="a",header=False)
            print("writing to CSV Now ....")          
        except FileNotFoundError as err:
            print("Errors in write to album data",err)

    def writeto_album_artists(self,keyword):
        alb_obj = Search()
        alb_data = alb_obj.search_album_artists(keyword)
        try:
            alb_data.to_csv("assets/album_artists.csv",mode="a",header=False)
            print("writing to CSV Now ....")          
        except FileNotFoundError:
            print("Error parsing the file")

    def writeto_album_Images(self,keyword):
        alb_obj = Search()
        alb_data = alb_obj.search_album_Images(keyword)
        try:
            alb_data.to_csv("assets/album_images.csv",mode="a",header=False)
            print("writing to CSV Now ....")          
        except FileNotFoundError:
            print("Error parsing the file")

    def write_playlist_tracks(self,play_id):
        track_ids = Search()
        time.sleep(1)
        all_tracks = track_ids.get_track_ids(play_id)
        try:
            with open("assets/play_trackIDS.txt","a") as playTracks:
                for track_id in all_tracks:
                    playTracks.write(track_id+"\n")
                    print("writing to file .....")

        except FileExistsError:
            print("Error the file needed cannot be reached")

        except FileNotFoundError:
            print("The file you are searching cannot be found ")