from django.urls import path 
from .views import ArtistSerializerList,ArtistInfoSerializer,ArtistInfoListSerializer


urlpatterns = [
    # subscribe to an Artist 
    path('artistSub/',ArtistSerializerList.as_view()),
    path('artistList/',ArtistInfoSerializer.as_view()),

    # subscribe to a certain info data as below seen.
    path('artistInfo/<str:pk>/',ArtistInfoListSerializer.as_view())
]