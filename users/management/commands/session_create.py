from datetime import timedelta

from django.core.management.base import BaseCommand
from faker import Faker
import random
from cinema.models import Film, Hall
from users.models import Session


class Command(BaseCommand):
    help = 'Generate 150 session'

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')
        film_id = Film.objects.all()
        hall_id = Hall.objects.all()



        for i in range(1, 10):
            for f in film_id:
                Session.objects.create(name=i, date=(f.release_date + timedelta(days= (random.randint(0, 6)))),
                                   dateTime=fake.time(pattern='%H:%M:%S'), film=f,
                                   hall=random.choice(hall_id), t2d=True, t3d=False,
                                   tIMAX=False)
