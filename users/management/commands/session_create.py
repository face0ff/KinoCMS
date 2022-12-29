import random

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from faker import Faker
import random

from cinema.models import Film, Hall
from gallerySeo.models import Image, Gallery, Seo
from pages.models import TemplatePage, MainPage, Contacts
from users.models import Session


class Command(BaseCommand):
    help = 'Generate random users'

    def handle(self, *args, **kwargs):
        # for i in ['О кинотеатре', 'Детская комната', 'Реклама', 'Кафе-бар', 'Vip-зал']:
        #     TemplatePage.objects.create(name=i, state='True', main='True', description=i,
        #                                 main_image='img/templatePage/empty-photo.png',
        #                                 gallery=Gallery.objects.create(),
        #                                 seo=Seo.objects.create(seo_title='test', seo_description='test',
        #                                                        seo_keywords='test', seo_url='http://test.ua'))
        # print("Записано")

        # MainPage.objects.create(phone='000000000', state='True', aditional_phone='000000000', seo_text='test',
        #                         seo=Seo.objects.create(seo_title='test', seo_description='test',
        #                                                seo_keywords='test', seo_url='http://test.ua'))
        # Contacts.objects.create(cinema_name='cinema_name', state='True', coordinate='coordinate', address='address',
        #                         logo='img/templatePage/empty-photo.png',
        #                         seo=Seo.objects.create(seo_title='test', seo_description='test',
        #
        #                                                seo_keywords='test', seo_url='http://test.ua'))
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