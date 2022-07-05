from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView,Response

from users.models import NewUser
from .serializers import HitJobSerializer,AlbumsSerializer, PlaylistSerializer, TrackSerializer,ArtistSerializer,SearchSerializer,ScheduleJobSerializer,UsersSerializer

from rest_framework import permissions,status
from .tasks import fetch_albumsDT,fetch_track_info
from spotAPI.models import Album,Track,Artist,Playlist
from scraper.search import search_all
from dateutil import parser 
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json

# Create your views here.
# your first quick experience as a medieval junior software engineer in Django and React

class StartNewWorker(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HitJobSerializer

    def post(self,request):
        name = request.data.get("target_name")
        serializer_class = HitJobSerializer

        #task scheduling ::
        celery_task1 = fetch_albumsDT.delay()
        trackinfo_task = fetch_track_info.delay()
        # fetch_artists = save_track_alb.delay()
        #DRF responses  to created tasks and tasks  in completion status undergoing testing phases

        return Response(
            data ={
                "result":f"job created for {name}",
                "celery_task2_id": celery_task1.id,
                "trackinfo_task": trackinfo_task.id,
                # "fetch_artists": fetch_artists.id
            },
            status = status.HTTP_200_OK
        )

class ScheduleNewWorker(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ScheduleJobSerializer

    def post(self,request):
        name = request.data.get("target_name")
        schedule_time = parser.parse(request.data.get("schedule_time"))
        # schedule time available here:
        schedule,_ = CrontabSchedule.objects.get_or_create(
            day_of_week = ",".join(request.data.get("days_of_week")),
            minute = schedule_time.minute,
            hour = schedule_time.hour,
        )

        new_celery_task = PeriodicTask.objects.update_or_create(
            name = f"Schedule hit job for {name}",
            defaults = {
                "task":"",
                "args": json.dumps([name]),
                "crontab":schedule
            },
        )

        return Response(
            data = {"result":"Task scheduled for execution"},
            status=status.HTTP_200_OK,
        )

class SearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SearchSerializer

    def post(self,request):
        query = request.data.get("keyword")
        # type = request.data.get("type")

        data_result = search_all(query,limit=10,offset=0)
        return Response(data=data_result,status = status.HTTP_200_OK)

class Users(APIView):
    '''
    Lists an Album and allow user create a new Album
    '''

    permission_classes = [permissions.IsAdminUser]
    def get(self,request,format=None):
        album = NewUser.objects.all()[1:30]
        serializer = UsersSerializer(album,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AlbumsList(APIView):
    '''
    Lists an Album and allow user create a new Album
    
    '''
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,format=None):
        album = Album.objects.all()[1:30]
        serializer = AlbumsSerializer(album,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = AlbumsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AlbumDetail(APIView):
    '''
    Performs actions of PUT,DELETE and RETREIVE on the object specified

    '''

    # permission_classes = [permissions.]

    def get_object(self,pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,format=None):
        album = self.get_object(pk)
        serializer = AlbumsSerializer(album)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        album = self.get_object(pk)
        serializer = AlbumsSerializer(album,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        album = self.get_object(pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TrackList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,format=None):
        tracklist = Track.objects.all()[:31]
        serializer = TrackSerializer(tracklist,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = TrackSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class TrackDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TrackSerializer

    '''
    serializer object for getting details related to tracks data

    '''
    def get_object(self,pk):
        try:
            Track.objects.get(pk)
        except Track.DoesNotExist:
            raise Http404
              
    def get(self,request,pk):
        track = self.get_object(pk)
        serializer = TrackSerializer(track)
        return Response(data=serializer.data)
    
    def put(self,request,pk):
        track_id = self.get_object(pk)
        serializer = TrackSerializer(track_id,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class Playlists(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,format=None):
        playlist = Playlist.objects.all()
        serializer = PlaylistSerializer(playlist,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = PlaylistSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class PlaylistDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    '''
    serializer object for getting details related to tracks data

    '''

    def get_object(self,pk):
        try:
            Playlist.objects.get(pk)
        except Playlist.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        playlist = self.get_object(pk)
        serializer = PlaylistSerializer(playlist)
        return Response(data=serializer.data)
    
    def put(self,request,pk):
        playlist_id = self.get_object(pk)
        serializer = PlaylistSerializer(playlist_id,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class Artists(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,format=None):
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = ArtistSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class ArtistDetail(APIView): 
    permission_classes = [permissions.IsAuthenticated]

    '''
    serializer object for getting details related to tracks data

    '''

    def get_object(self,pk):
        try:
            Artist.objects.get(pk)
        except Track.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        track = self.get_object(pk)
        serializer = ArtistSerializer(track)
        return Response(data=serializer.data)

    def put(self,request,pk):
        track_id = self.get_object(pk)
        serializer = ArtistSerializer(track_id,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

