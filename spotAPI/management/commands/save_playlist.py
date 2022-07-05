import csv
from django.core.management import BaseCommand
from django.utils import timezone
from spotAPI.models import Playlist
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = "help save playlist objects to database:"
    # def add_arguments(self, parser):
    # parser.add_argument("file_path", type=str)
    #this handler command saves playlists to database
    
    def handle(self, *args, **options):
        start_time = timezone.now()
        # file_path = options["file_path"]
        with open("assets/playlist_data.csv","r",encoding="utf8") as csv_file:
            data = csv.reader(csv_file,delimiter=",")
            playlists = {art.play_SpotID : art for art in Playlist.objects.all()}
            
            for row in data:
                try:
                    play_name = row[1]
                    play_id = row[5]
                    play_Href = row[4]
                    play_Descrition = row[3]
                    play_collabs = row[2]
                    play_types = row[6]
                    play_total_tracks = row[7]

                    play_ID  = playlists.get(play_id)
                    artist_dt = []
                    if not play_ID:
                        play_ID = Playlist.objects.create(
                            play_SpotID = play_id,
                            play_Name = play_name,
                            play_Href = play_Href,
                            play_Descrition = play_Descrition,
                            play_collabs = play_collabs,
                            play_types = play_types,
                            play_total_tracks = play_total_tracks
                        )
                        playlists[play_ID.play_SpotID] = play_ID

                    play_info = Playlist(
                        play_SpotID = play_id,
                        play_Name = play_name,
                        play_Href = play_Href,
                        play_Descrition = play_Descrition,
                        play_collabs = play_collabs,
                        play_types = play_types,
                        play_total_tracks = play_total_tracks
                    )
                    
                    artist_dt.append(play_info)
                    if len(artist_dt) > 5000:
                        try:
                            Playlist.objects.bulk_create(artist_dt)
                            artist_dt = []
                        except IntegrityError:
                            continue
                    if artist_dt:
                        Playlist.objects.create(artist_dt)
                except:
                    continue

        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )