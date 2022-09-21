from rest_framework import serializers
from Subs.models import Artist,Label,ArtistInfo
from users.serializers import UserSerializer

class ArtistSerializer(serializers.ModelSerializer):
    # owner = UserSerializer() to get owner serialized data
    class Meta:
        model = Artist
        fields = ['id','name','owner']

class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = '__all__'

class ArtistInfoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ArtistInfo
        fields = '__all__'
        
