from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('users/', views.users_view, name='users'),
    path('users/register/', views.create_user, name='create_user'),
    path('users/login_page/', views.login_page, name='login_page'),
    path('users/logout_page/', views.logout_page, name='logout_page'),
    path('users/users_delete/<int:pk>/', views.users_delete, name='users_delete'),
    path('users/users_update/<int:pk>/', views.users_update, name='users_update'),
    path('mail/', views.mail_view, name='mail'),
    path('mail/delete/<int:pk>/', views.mail_delete, name='mail_delete'),
    path('mail/show_percent/', views.show_percent, name='show_percent'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)