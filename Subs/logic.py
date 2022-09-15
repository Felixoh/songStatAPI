#logic  to save data to object created by user
from .models import Artist 
from .models import ArtistInfo
from .models import Label

def get_al_user_artists(pk):
    art = Artist.objects.all()
    return art 
