from django.db import models
from  users.models import NewUser

# Create your models here.
class Track(models.Model): 
    track_Name = models.CharField(max_length=255,null=True)
    track_SpotID = models.CharField(max_length=150,primary_key=True)
    track_No = models.IntegerField(null=True)
    track_Type = models.CharField(max_length=255,null=True)
    track_Popularity = models.IntegerField(null=True)
    track_duration = models.BigIntegerField(null=True)
    track_discNo = models.IntegerField(null=True)
    
    def __str__(self):  
        return self.track_Name or ''
        
class Playlist(models.Model):
    play_SpotID = models.CharField(max_length=150,primary_key=True)
    play_Name = models.CharField(max_length=255)
    play_Href = models.CharField(max_length=200)
    play_Descrition = models.CharField(max_length=255)
    play_collabs = models.CharField(max_length=150)
    play_types = models.CharField(max_length=150)
    play_total_tracks = models.IntegerField()

    def __str__(self): 
        return self.play_Name
 
class Album(models.Model):
    alb_SpotID = models.CharField(max_length=255,primary_key=True)
    alb_Name = models.CharField(max_length=255)
    alb_Type = models.CharField(max_length=255)
    alb_Href = models.URLField()
    alb_ReleaseDate = models.CharField(max_length=50)
    alb_ReleaseDatePrecision = models.CharField(max_length=10)
    alb_URI = models.URLField()
    alb_total_tracks = models.IntegerField()
    #fKeys
    trackID = models.ForeignKey(Track,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.alb_Name or ''

class Artist(models.Model):
    art_SpotID = models.CharField(max_length=255,primary_key=True)
    art_Name = models.CharField(max_length=255,null=True)
    art_Popularity = models.CharField(max_length=255,null=True) 
    art_URI = models.URLField(null=True)
    art_type = models.CharField(max_length=255,null=True)
    art_HREF = models.URLField(null=True)
    art_followers = models.IntegerField(null=True)

    #fkeys
    alb_ID = models.ForeignKey(Album,null=True,on_delete=models.CASCADE)
    trackID = models.ForeignKey(Track,null=True,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.art_Name or ''

class Image(models.Model):
    img_Height = models.IntegerField()
    img_Width = models.IntegerField()
    img_URI = models.URLField()

    #fkeys 
    albID = models.ForeignKey(Album,on_delete=models.CASCADE,null=True)
    artID = models.ForeignKey(Artist,on_delete=models.CASCADE,null=True)
    playID = models.ForeignKey(Playlist,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.img_Height
