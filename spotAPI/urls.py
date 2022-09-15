from django.urls import path
from .views import   AlbumDetail,StartNewWorker,ScheduleNewWorker,AlbumsList, TrackDetail, TrackList,Playlists,PlaylistDetail,Artists,ArtistDetail,SearchView,Users

urlpatterns = [
    #users management 
    path('users/',Users.as_view()),

    #periodic scheduling task endpoints ...
    path('newtask/',StartNewWorker.as_view()),
    path('schedule/',ScheduleNewWorker.as_view()),
    
    path('albums/',AlbumsList.as_view()),
    path('albums/<str:pk>/',AlbumDetail.as_view()),
    
    #tracks
    path('tracks/',TrackList.as_view()),
    path('tracks/<str:pk>/',TrackDetail.as_view()),
    
    #playlist
    path('playlist/',Playlists.as_view()),
    path('playlist/<str:pk>/',PlaylistDetail.as_view()),

    #Artist
    path('artists/',Artists.as_view()),
    path('artists/<str:pk>',ArtistDetail.as_view()),
    
    #search
    path('search/',SearchView.as_view())
    #filter to get latest music/artist/playlistIDs from database
    
]
