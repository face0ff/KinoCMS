import datetime

from django.core.management.base import BaseCommand
from faker import Faker

from banners.models import BannerBackground, BannerUp, BannerNews, BannerNewsPromo, BannerMainUp
from cinema.models import Cinema, Hall, Film
from gallerySeo.models import Image, Gallery, Seo
from pages.models import TemplatePage, MainPage, Contacts, NewsPromotions
from users.models import Mail


class Command(BaseCommand):
    help = 'Generate random users'

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')
        url = 'https://banner.com'
        if BannerUp.objects.count() == 0:
            BannerUp.objects.create(id=1)
            print('BannerUp create successful')
        if BannerNews.objects.count() == 0:
            BannerNews.objects.create(id=1)
            print('BannerNews create successful')
        if BannerBackground.objects.count() == 0:
            BannerBackground.objects.create(id=1, color=fake.hex_color(), imageBackground='#',
                                            background=True)
            print('BannerBackground create successful')
        if BannerNewsPromo.objects.count() == 0:
            for index in range(3):
                b = BannerNewsPromo()
                b.url = url
                b.promo = True
                b.image = '#'
                b.banner_news = BannerNews.objects.get(pk=1)
                b.save()
            print('BannerNewsPromo create successful')
        if BannerMainUp.objects.count() == 0:
            for index in range(3):
                b = BannerMainUp()
                b.url = url
                b.text = 'test'
                b.image = '#'
                b.banner_up = BannerUp.objects.get(pk=1)
                b.save()
            print('BannerMainUp create successful')
        if TemplatePage.objects.count() == 0:
            list = ['О кинотеатре', 'Реклама', 'Кафе-бар', 'Мобильное приложение', 'Vip-зал', 'Детская комната']
            for i in list:
                TemplatePage.objects.create(id=(list.index(i) + 1), name=i, state='True', main='True', description=i,
                                            main_image='#',
                                            gallery=Gallery.objects.create(),
                                            seo=Seo.objects.create(seo_title='test', seo_description='test',
                                                                   seo_keywords='test', seo_url='http://test.ua'))
            print("Записано")
        if MainPage.objects.count() == 0:
            MainPage.objects.create(id=1, phone=fake.phone_number(), state='True', aditional_phone=fake.phone_number(),
                                    seo_text='test',
                                    seo=Seo.objects.create(seo_title='test', seo_description='test', seo_keywords='test'
                                                           , seo_url='http://test.ua'))

        if Contacts.objects.count() == 0:
            Contacts.objects.create(id=1, cinema_name='Звездный', state='True',
                                    coordinate='46.57317928816355, 30.78472948814475', address='Одесса',
                                    logo='#',
                                    seo=Seo.objects.create(seo_title='test', seo_description='test',
                                                           seo_keywords='test', seo_url='http://test.ua'))
        if Cinema.objects.count() == 0:
            Cinema.objects.create(name='Звездный', description='Звездный',
                                  condition='Звездный',
                                  logo='#',
                                  banner_up_image='#',
                                  seo=Seo.objects.create(seo_title='test', seo_description='test',
                                                         seo_keywords='test', seo_url='http://test.ua'),
                                  gallery=Gallery.objects.create())

        if Hall.objects.count() == 0:
            cinemas = Cinema.objects.all()
            for i in cinemas:
                Hall.objects.create(number='1', description='test', create_date=datetime.date.today(),
                                    scheme='#',
                                    banner_up_image='#', cinema=i,
                                    seo=Seo.objects.create(seo_title='test', seo_description='test',
                                                           seo_keywords='test', seo_url='http://test.ua'),
                                    gallery=Gallery.objects.create())

        if Film.objects.count() == 0:
            films = [['Интерстеллар', 'Интер укр'], ['Джанго', 'Джанго укр'],
                     ['Шазам', 'Шазам укр'],
                     ['Хранители', 'Хранители укр']]
            trailer_url = ["https://www.youtube.com/embed/qcPfI0y7wRU",
                           "https://www.youtube.com/embed/4McenUEna3E",
                           "https://www.youtube.com/embed/rvJdxDjn6nI",
                           "https://www.youtube.com/embed/12q2pDWPuyI"]

            for i in films:
                Film.objects.create(title_ru=i[0], title_uk=i[1], description_ru=fake.text(max_nb_chars=100),
                                    description_uk=fake.text(max_nb_chars=100),
                                    release_date=fake.date_between_dates(date_start='-10days', date_end='+10days'),
                                    main_image='#',
                                    trailer_url=trailer_url[(films.index(i))],
                                    type2d=fake.boolean(), type3d=fake.boolean(), typeIMAX=fake.boolean(),
                                    seo=Seo.objects.create(seo_title='test', seo_description='test',
                                                           seo_keywords='test', seo_url='http://test.ua'),
                                    gallery=Gallery.objects.create())
        if Mail.objects.count() == 0:
            Mail.objects.create(HtmlTemplate='file/mail/mail_test.html')
            print('все идет как надо')
        if NewsPromotions.objects.count() == 0:
            for index in range(6):
                news_promo = NewsPromotions()
                news_promo.seo = Seo.objects.create(seo_title='test', seo_description='test',
                                                        seo_keywords='test', seo_url='http://test.ua')
                news_promo.gallery = Gallery.objects.create()
                news_promo.name_ru = fake.text(max_nb_chars=10)
                news_promo.name_uk = fake.text(max_nb_chars=10)
                news_promo.state = fake.boolean()
                news_promo.date_publication = fake.date_between_dates(date_start='now', date_end='+10days')
                news_promo.video_url = index
                news_promo.main_image = '#'
                news_promo.is_promotions = fake.boolean()
                news_promo.description_ru = fake.text(max_nb_chars=100)
                news_promo.description_uk = fake.text(max_nb_chars=100)
                news_promo.save()
