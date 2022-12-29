from django.core.management.base import BaseCommand

from gallerySeo.models import Image, Gallery, Seo
from pages.models import TemplatePage, MainPage, Contacts


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
        Contacts.objects.create(cinema_name='cinema_name', state='True', coordinate='coordinate', address='address',
                                logo='img/templatePage/empty-photo.png',
                                seo=Seo.objects.create(seo_title='test', seo_description='test',
                                                       seo_keywords='test', seo_url='http://test.ua'))