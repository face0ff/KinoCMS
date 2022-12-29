from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.banners_view, name='banners'),
    # path('delete/<int:pk>/', views.delete_back, name="delete_back"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)