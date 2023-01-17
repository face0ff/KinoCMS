from django.shortcuts import get_object_or_404

from banners.models import BannerBackground
from pages.models import MainPage, TemplatePage, Contacts


def welcome(request):
    banners_back = get_object_or_404(BannerBackground, pk=1)
    phone = get_object_or_404(MainPage, pk=1)
    pages = TemplatePage.objects.filter(state=True)
    contacts = Contacts.objects.filter(state=True)
    return {
        'contacts': contacts,
        'pages': pages,
        'banners_back': banners_back,
        'phone': phone,
        }