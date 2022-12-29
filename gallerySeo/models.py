from django.db import models


class Seo(models.Model):
    seo_url = models.URLField("Ссылка")
    seo_title = models.CharField("Название", max_length=150)
    seo_keywords = models.CharField("Слова", max_length=150)
    seo_description = models.TextField("Описание")


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Gallery'


class Image(models.Model):
    image = models.ImageField("Изображение", upload_to="img/")
    gallery = models.ForeignKey(Gallery,
                                on_delete=models.CASCADE, null=True)
