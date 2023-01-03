
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
        for i in range(1, 50):

            Session.objects.create(id=i, name=i, date=fake.date_this_month(after_today=True),
                                   dateTime=fake.time(pattern='%H:%M:%S'),film=random.choice(film_id),
                                   hall=random.choice(hall_id), t2d=True, t3d=False,
                                   tIMAX=False)
        for i in range(50, 100):

            Session.objects.create(id=i, name=i, date=fake.date_this_month(after_today=True),
                                   dateTime=fake.time(pattern='%H:%M:%S'),film=random.choice(film_id),
                                   hall=random.choice(hall_id), t2d=False, t3d=True,
                                   tIMAX=False)

        for i in range(100, 150):

            Session.objects.create(id=i, name=i, date=fake.date_this_month(after_today=True),
                                   dateTime=fake.time(pattern='%H:%M:%S'),film=random.choice(film_id),
                                   hall=random.choice(hall_id), t2d=False, t3d=False,
                                   tIMAX=True)