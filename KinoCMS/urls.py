from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import cinema
from django.conf.urls.i18n import i18n_patterns
from cinema.views import kino_cms

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),



] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path("adminlte/", include('adminLte.urls')),
    path('', kino_cms, name='kino_cms'),
    path('poster/<int:pk>/', cinema.views.poster, name='poster'),
    path('promotions_site/', cinema.views.promotions_site, name='promotions_site'),
    path('promotion_site/<int:pk>/', cinema.views.promotion_site, name='promotion_site'),
    path('booking/<int:pk>/', cinema.views.booking, name='booking'),
    path('film_card/<int:pk>/', cinema.views.film_card, name='film_card'),
    path('cinema_card/<int:pk>/hall_card/<int:pk_alt>/', cinema.views.hall_card, name='hall_card'),
    path('cinema_site/', cinema.views.cinema_site, name='cinema_site'),
    path('sessions/', cinema.views.sessions, name='sessions'),
    path('sessions/<int:pk>/', cinema.views.sessions, name='sessions'),
    path('cinema_card/<int:pk>/', cinema.views.cinema_card, name='cinema_card'),
    path('film_card/show_session/', cinema.views.show_session, name='show_session'),
    path('film_card/select_session/', cinema.views.select_session, name='select_session'),
    path('sessions/filter_session/', cinema.views.filter_session, name='filter_session'),
    path('sessions/filter_session_all/', cinema.views.filter_session_all, name='filter_session_all'),
    path('sessions/filter_film/', cinema.views.filter_film, name='filter_film'),
    path('sessions/filter_cinema/', cinema.views.filter_cinema, name='filter_cinema'),
    path('sessions/filter_hall/', cinema.views.filter_hall, name='filter_hall'),
    path('booking/list_booking/', cinema.views.list_booking, name='list_booking'),
    path('booking/del_booking/', cinema.views.del_booking, name='del_booking')
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
