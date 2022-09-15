from django.contrib import admin
from Subs.models import Artist,Label,ArtistInfo

# Register your models here.
admin.site.register(Artist)
admin.site.register(Label)
admin.site.register(ArtistInfo)
