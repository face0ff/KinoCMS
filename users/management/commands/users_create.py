import random

from faker import Faker
from django.core.management.base import BaseCommand

from gallerySeo.models import Image, Gallery, Seo
from pages.models import TemplatePage, MainPage, Contacts
from users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='how many sessions generate')

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        for _ in range(options['number']):
            user = User.objects.create_user(
                address=fake.street_address(),
                city=fake.city(),
                name=fake.first_name(),
                surname=fake.last_name(),
                phone='+9999999999',
                card_number=fake.credit_card_number(),
                birthday_date=fake.date_of_birth(minimum_age=7, maximum_age=105),
                email=fake.email(),
                language=random.choice(['ru', 'uk']),
                gender=random.choice(['m', 'f']),
                password='1234',
                username=fake.simple_profile()['username'],
            )
            print('User **'+user.username+'** successfully create')