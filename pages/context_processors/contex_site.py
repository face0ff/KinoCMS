from django.shortcuts import get_object_or_404

from banners.models import BannerBackground
from pages.models import MainPage, TemplatePage, Contacts, NewsPromotions


def welcome(request):
    banners_back = get_object_or_404(BannerBackground, pk=1)
    phone = get_object_or_404(MainPage, pk=1)
    pages = TemplatePage.objects.filter(state=True)
    contacts = Contacts.objects.filter(state=True)
    news = NewsPromotions.objects.filter(is_promotions=False, state=True)
    return {
        'news': news,
        'contacts': contacts,
        'pages': pages,
        'banners_back': banners_back,
        'phone': phone,
        }