from django.contrib import admin
from .models import *

class MusicStatAdminArea(admin.AdminSite):
    site_header = 'MusicStatsAdmin'

musicApp = MusicStatAdminArea(name="MusicStats Admin")
# Register your models here.
# musicApp.register(Track)
# musicApp.register(Playlist)
# musicApp.register(Album)
# musicApp.register(Image)
# musicApp.register(Artist)

admin.site.register(Track)
admin.site.register(Playlist)
admin.site.register(Album)
admin.site.register(Image)
admin.site.register(Artist)
