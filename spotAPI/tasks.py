from celery import shared_task
# from scraper.save_DB import save_artistDT

#initialise our scraper tasks with celery from this point:
from scraper.concurrent import Concurrent
conc = Concurrent()

@shared_task
def fetch_artists():
    Concurrent(workers=20).fetch_artist_info() 

