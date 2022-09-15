from django.shortcuts import render
from Subs.models import Artist
from rest_framework.views import APIView,Response 
from rest_framework import permissions,status 
from django.http import Http404

# local imports 
from .serializers import ArtistSerializer,LabelSerializer,ArtistInfoSerializers
from .permissions import IsFreePlan,ISAdminOnly
from .models import Artist,Label
from users.models import NewUser 
# from spotAPI.tasks import save_artistInfo

class ArtistSerializerList(APIView):
    # serialize data used from our article information related datas.
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated,IsFreePlan]
    
    def get(self,request,format=None):
        query = Artist.objects.filter(owner=request.user)
        
        serializer = ArtistSerializer(query,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        # get user data and send our personalised request data to the database
        name = request.data.get("name")

        serializer = ArtistSerializer(data={"owner":request.user.id,"name":name})

        # save serialized data
        if serializer.is_valid():
            serializer.save()
            
            # save related object data to database now assyncronously.
           
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id):
        pass

    def delete(self,request,format=None):
        pass

# Now get my customer's personalised data and statistics to view here.
# call the user 

class ArtistInfoSerializer(APIView):
    permission_classes = [permissions.IsAuthenticated,IsFreePlan]
    message = "you are not permitted to view this page if not on Free Plan"

    def get(self,request,format=None):
        owner = request.user.id 
        artist = NewUser.objects.get(id=owner)
        art_data = artist.artist_set.all()

        serializer = ArtistSerializer(art_data,many=True)
        return Response(serializer.data)

class ArtistInfoListSerializer(APIView):
    permission_classes = [permissions.IsAuthenticated,IsFreePlan]
    message = "you are not permitted to view this page if not on Free Plan"

    def get_object(self,pk):
        try:
            Artist.objects.get(pk)
        except Artist.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        objc = self.get_object(pk)
        artist_infoList = objc.artInfo.all()
        serializer = ArtistInfoSerializers(artist_infoList,many=True)
        return Response(serializer.data)