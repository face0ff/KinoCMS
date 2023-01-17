from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('pages/', views.pages_view, name='pages'),
    path('pages/delete/<int:pk>/', views.pages_delete, name='pages_delete'),
    path('pages/pages_create', views.pages_create, name='pages_create'),
    path('pages/pages_create/pages_update/<int:pk>/', views.pages_update, name='pages_update'),
    path('pages/main_update/<int:pk>/', views.main_update, name='main_update'),
    path('pages/contacts_update/', views.contacts_update, name='contacts_update'),
    path('news/', views.news_view, name='news'),
    path('news/delete/<int:pk>/', views.news_delete, name='news_delete'),
    path('news/news_create/', views.news_create, name='news_create'),
    path('news/news_update/<int:pk>/', views.news_update, name='news_update'),
    path('promotions/', views.promotions_view, name='promotions'),
    path('promotions/delete/<int:pk>/', views.promotions_delete, name='promotions_delete'),
    path('promotions/promotions_create/', views.promotions_create, name='promotions_create'),
    path('promotions/promotions_update/<int:pk>/', views.promotions_update, name='promotions_update'),
    path('pages/user_editing/<int:pk>/', views.user_editing, name='user_editing'),
    # path('about_site/', views.about_site, name='about_site'),
    # path('bar_site/', views.bar_site, name='bar_site'),
    # path('apk_site/', views.apk_site, name='apk_site'),
    path('contacts_site/', views.contacts_site, name='contacts_site'),
    # path('vip_site/', views.vip_site, name='vip_site'),
    # path('advert_site/', views.advert_site, name='advert_site'),
    # path('kids_site/', views.kids_site, name='kids_site'),
    path('news_site/', views.news_site, name='news_site'),
    path('info_pages/<int:pk>/', views.info_pages, name='info_pages'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)