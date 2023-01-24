from django.db import models
from django.contrib.auth.models import AbstractUser

from cinema.models import Film, Hall


class User(AbstractUser):
    CHOISES_language = [('uk', 'Українська'), ('ru', 'Русский')]
    CHOISES_gender = [('m', 'Муж.'), ('f', 'Жен.')]
    name = models.CharField("Имя", max_length=32)
    surname = models.CharField("Фамилия", max_length=32)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField("Фамилия", max_length=150)
    # password = models.CharField("Ник", max_length=32)
    card_number = models.CharField("Номер карты", max_length=19)
    gender = models.CharField(max_length=10, choices=CHOISES_gender)
    language = models.CharField(max_length=10, choices=CHOISES_language)
    phone = models.CharField(max_length=16, blank=True)
    birthday_date = models.DateField("Дата рождения", null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    # confirm_password = models.CharField("Пароль", max_length=32)
    city = models.CharField("Город", max_length=32)


class Session(models.Model):
    name = models.CharField("Сессия", max_length=32, default="Номер1")
    date = models.DateField("Дата сеанса", null=True)
    dateTime = models.TimeField("Дата сеанса", null=True)
    t2d = models.BooleanField("2d", default=True)
    t3d = models.BooleanField("3d", default=False)
    tIMAX = models.BooleanField("IMAX", default=False)

    film = models.ForeignKey(Film,
                             on_delete=models.CASCADE, null=True)
    hall = models.ForeignKey(Hall,
                             on_delete=models.CASCADE, null=True)


class Tiket(models.Model):
    row = models.PositiveSmallIntegerField("Ряд", default=0)
    price = models.PositiveSmallIntegerField("Цена", default=0)
    place = models.PositiveSmallIntegerField("Место", default=0)
    booking = models.BooleanField("Бронь")
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session,
                                on_delete=models.CASCADE, null=True)


class Mail(models.Model):
    HtmlTemplate = models.FileField("Рассылка", upload_to="file/mail/", blank=True)
    date_added = models.DateTimeField(auto_now=True)

