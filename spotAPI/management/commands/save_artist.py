import csv
from tarfile import NUL
from django.core.management import BaseCommand
from django.utils import timezone
from spotAPI.models import Artist
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = "help save playlist objects to database:"
    # def add_arguments(self, parser):
    # parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        # file_path = options["file_path"]
        # this handler saves all artist info to database.
        
        with open("assets/artistinfo_csv.csv","r",encoding="utf8") as csv_file:
            data = csv.reader(csv_file,delimiter=",")
            artists = {art.art_SpotID : art for art in Artist.objects.all()}

            artist_dt = []
            for row in data:
                try:
                    art_SpotID = row[8]
                    art_ID  = artists.get(art_SpotID)

                    
                    if not art_ID:
                        art_IDS = Artist.objects.create(
                            art_SpotID= row[8],
                            art_Name = row[1],
                            art_popularity = row[4],
                            art_URI = row[6],
                            art_type = row[5],
                            art_HREF = row[7],
                            art_followers = row[3],
                            alb_ID = row[2]

                        )
                        
                        artists[art_ID.art_SpotID] = art_IDS

                    art_info = Artist(
                        art_SpotID= row[8],
                        art_Name = row[1],
                        art_popularity = row[4],
                        art_URI = row[6],
                        art_type = row[5],
                        art_HREF = row[7],
                        art_followers = row[3],
                        #fkeys
                        # alb_ID = NUL,
                        # trackID = NUL
                    )

                    artist_dt.append(art_info)
                    if len(artist_dt) > 5000:
                        try:
                            Artist.objects.bulk_create(artist_dt)
                            artist_dt = []
                        except IntegrityError as e:
                            continue
                    if artist_dt:
                        Artist.objects.create(artist_dt)
                except:
                    continue

        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )