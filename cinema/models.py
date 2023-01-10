from django.db import models

from gallerySeo.models import Seo, Gallery



class Film(models.Model):
    title = models.CharField("Фильм", max_length=32)
    description = models.TextField("Описание")
    main_image = models.ImageField("Главное изображение", upload_to="img/films/")
    trailer_url = models.URLField(unique=False)
    release_date = models.DateField("Примьера в мире", null=False, blank=False)
    type2d = models.BooleanField("2d")
    type3d = models.BooleanField("3d")
    typeIMAX = models.BooleanField("IMAX")
    seo = models.OneToOneField(Seo,
                               on_delete=models.CASCADE, null=True)
    gallery = models.OneToOneField(Gallery,
                                   on_delete=models.CASCADE, null=True)


class Cinema(models.Model):
    name = models.CharField("Кинотеатр", max_length=32)
    description = models.TextField("Описание")
    condition = models.TextField("Описание")
    logo = models.ImageField("Лого", upload_to="img/cinema/")
    banner_up_image = models.ImageField("Баннер", upload_to="img/cinema/")
    seo = models.OneToOneField(Seo,
                               on_delete=models.CASCADE, null=True)
    gallery = models.OneToOneField(Gallery,
                                   on_delete=models.CASCADE, null=True)


class Hall(models.Model):
    number = models.CharField("{% trans 'Номер зала' %}", max_length=3)
    description = models.TextField("Описание")
    scheme = models.ImageField("План зала", upload_to="img/hall/")
    banner_up_image = models.ImageField("Баннер", upload_to="img/hall/")
    create_date = models.DateField("Дата создания",  null=False, blank=False)
    cinema = models.ForeignKey(Cinema,
                               on_delete=models.CASCADE, null=True)
    seo = models.OneToOneField(Seo,
                               on_delete= models.CASCADE, null=True)
    gallery = models.OneToOneField(Gallery,
                                   on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('number', 'cinema')


