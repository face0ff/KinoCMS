from django.db import models
from gallerySeo.models import Seo, Gallery


class MainPage(models.Model):
    state = models.BooleanField("Состояние")
    phone = models.CharField(max_length=17, blank=True)
    aditional_phone = models.CharField(max_length=17, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    seo_text = models.TextField("Описание")
    seo = models.OneToOneField(Seo,
                               on_delete=models.PROTECT, null=True)


class TemplatePage(models.Model):
    state = models.BooleanField("Состояние")
    main = models.BooleanField("Поле", default=False)
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    main_image = models.ImageField("Главное изображение", upload_to="img/templatePage/")
    date_publication = models.DateTimeField(auto_now_add=True)
    seo = models.OneToOneField(Seo,
                               on_delete=models.PROTECT, null=True)
    gallery = models.OneToOneField(Gallery,
                                   on_delete=models.PROTECT, null=True)


class Contacts(models.Model):
    state = models.BooleanField("Состояние")
    cinema_name = models.CharField("Название", max_length=32,  null=True)
    address = models.TextField("Описание", null=False)
    date_publication = models.DateTimeField(auto_now_add=True)
    coordinate = models.TextField("Координаты", null=True)
    logo = models.ImageField("Изображение", upload_to="img/contacts/")
    seo = models.OneToOneField(Seo,
                               on_delete=models.PROTECT, null=True)


class NewsPromotions(models.Model):
    state = models.BooleanField("Состояние")
    name = models.CharField("Название", max_length=32)
    description = models.TextField("Описание")
    date_publication = models.DateField("Примьера в мире", null=True, blank=True)
    main_image = models.ImageField("Главное изображение", upload_to="img/newsPromotions/")
    video_url = models.URLField(unique=False)
    is_promotions = models.BooleanField("Состояние", default=False)
    seo = models.OneToOneField(Seo,
                               on_delete=models.PROTECT, null=True)
    gallery = models.OneToOneField(Gallery,
                                   on_delete=models.PROTECT, null=True)



