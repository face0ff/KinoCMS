from django.urls import path, include

import cinema
from .views import stat_view
from django.conf.urls.i18n import i18n_patterns
# from . import views

urlpatterns = [
    path('', stat_view, name='stat'),
    path('', include('cinema.urls')),
    path('banners/', include('banners.urls')),
    path('pages/', include('pages.urls')),
    path('user/', include('users.urls')),
]
