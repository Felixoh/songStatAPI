import csv
from tarfile import NUL
from django.core.management import BaseCommand
from django.utils import timezone
from spotAPI.models import Artist,Album,Track
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = "help save playlist objects to database:"
    # def add_arguments(self, parser):
    # parser.add_argument("file_path", type=str)
    # this handler saves all scraped album to dtabase

    def handle(self, *args, **options):
        start_time = timezone.now()
        # file_path = options["file_path"]
        with open("assets/album_data.csv","r",encoding="utf8") as csv_file:
            data = csv.reader(csv_file,delimiter=",")
            Albs = {art.alb_SpotID : art for art in Album.objects.all()}

            for row in data:
                try:
                    alb_SpotID=  row[9]

                    Alb_ID  = Albs.get(alb_SpotID)
                    artist_dt = []
                    if not Alb_ID:
                        Alb_ID = Album.objects.create(
                            alb_SpotID = row[9],
                            alb_Name= row[3],
                            alb_Type = row[7],
                            alb_Href = row[2],
                            alb_ReleaseDate = row[4],
                            alb_ReleaseDatePrecision= row[5],
                            alb_URI  = row[8],
                            alb_total_tracks = row[6] 
                            #fkeys
                        )
                        #going rounds and rounds in sync
                        Albs[Alb_ID.alb_SpotID] = Alb_ID

                    art_info = Album(
                            alb_SpotID = row[9],
                            alb_Name= row[3],
                            alb_Type = row[7],
                            alb_Href = row[2],
                            alb_ReleaseDate = row[4],
                            alb_ReleaseDatePrecision= row[5],
                            alb_URI  = row[8],
                            alb_total_tracks = row[6] 
                            #fkeys
                    )

                    artist_dt.append(art_info)
                    if len(artist_dt) > 5000:
                        try:
                            Album.objects.bulk_create(artist_dt)
                            artist_dt = []
                        except IntegrityError:
                            continue
                    if artist_dt:
                        Album.objects.create(artist_dt)
                except:
                    continue

        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )