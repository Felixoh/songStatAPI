from django.db import models
from rest_framework.response import Response
from rest_framework import permissions,status,serializers
from users.models import NewUser
from django.dispatch import receiver
from django.db.models.signals import post_save
# from spotAPI.tasks import save_artistInfo
import csv

# Create your models here
class Artist(models.Model):
    owner = models.ForeignKey(to=NewUser,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=50)
    artists = models.ForeignKey(Artist,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

@receiver(post_save,sender=Artist)
def create_artistInfo(sender,instance,*args,**kwargs):
    if instance:
        # celery_task1 = save_artistInfo.delay(art_obj,name)
        with open("assets/artistInfo_csv.csv","r",encoding="utf8") as csv_file:
            data = csv.reader(csv_file,delimiter=",")
            artists = {art.name : art for art in Artist.objects.all()}
            
            for row in data:
                try:
                    art_name = row[1]
                    art_id = row[2]
                    art_follower = row[3]
                    art_popularity = row[4]
                    art_type = row[5]
                    art_uri = row[6]
                    art_href = row[7]

                    art_Name = artists.get(art_name)
                    artist_dt = []

                    if art_Name:
                        ArtistInfo.objects.create(
                            # artist=artists.get(id),
                            artist=instance,
                            art_id = art_id,
                            art_followers = art_follower,
                            art_popularity = art_popularity,
                            art_type = art_type,
                            art_URI = art_uri,
                            art_href = art_href
                        )
                except:
                    pass 
        # ArtistInfo.objects.create(artist=instance,)

class ArtistInfo(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name="artInfo")
    # art_name = models.CharField(max_length=100)
    art_id = models.CharField(max_length=100)
    art_followers = models.IntegerField(blank=True,null=True)
    art_popularity = models.IntegerField(blank=True,null=True)
    art_type = models.CharField(max_length=50,blank=True)
    art_URI = models.CharField(max_length=100,blank=True)
    art_href = models.CharField(max_length=100,blank=True)
    
    def __str__(self):

        return self.artist.name