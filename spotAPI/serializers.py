from rest_framework import serializers
from users.models import NewUser
from spotAPI.models import Album,Track,Playlist,Artist

class UsersSerializer(serializers.ModelSerializer):
    
    '''
    Model serializers to list and preview account details about the system users:
    '''
    
    class Meta:
        model = NewUser
        fields = '__all__'

class HitJobSerializer(serializers.Serializer):
    '''
    redis simple request for scraper to start execution of assyncronous tasks behind the scenes.

    '''
    target_name = serializers.CharField(allow_blank=False,min_length=2,max_length=400)

    class Meta:
        fields = "target_name"

class SearchSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=200)
    # type = serializers.CharField(max_length=150)

    class Meta: 
        fields = "keyword"

class ScheduleJobSerializer(serializers.Serializer):
    target_name = serializers.CharField(allow_blank=False,min_length=2,max_length=400)
    days_of_week = serializers.CharField()
    schedule_time = serializers.DateTimeField()

    class Meta:
        fields = ("target_name","days_of_week","schedule_time")

class AlbumsSerializer(serializers.ModelSerializer):
    '''
    serializer class for all model instances passed along.
    ''' 
    class Meta:
        model = Album
        fields = [
            'alb_SpotID',
            'alb_Name',
            'alb_Type',
            'alb_Href',
            'alb_ReleaseDate',
            'alb_ReleaseDatePrecision',
            'alb_URI']

class TrackSerializer(serializers.ModelSerializer):
    '''
    model serializer for track information
    '''
    class Meta:
        model = Track
        fields = [
            'track_Name',
            'track_SpotID',
            'track_No',
            'track_Type',
            'track_Popularity',
            'track_duration',
            'track_discNo'
        ]
        
class PlaylistSerializer(serializers.ModelSerializer):
    '''
    model instance to fetch related artist information to all artists:
    '''
    class Meta:
        model = Playlist
        fields = [
            'play_SpotID',
            'play_Name',
            'play_Href',
            'play_Descrition',
            'play_collabs',
            'play_types',
            'play_total_tracks'
        ]

class ArtistSerializer(serializers.ModelSerializer):
    '''
    serializer for information related to an Artist
    '''
    class Meta:
        model = Artist
        fields = [
            'art_SpotID',
            'art_Name',
            'art_Popularity',
            'art_URI',
            'art_type',
            'art_HREF',
            'art_followers'
        ]
