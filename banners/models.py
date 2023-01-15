from django.db import models


class BannerNews(models.Model):
    class Speed(models.IntegerChoices):
        FIVE_SEC = 5000, '5с'
        TEN_SEC = 10000, '10с'
        FIFTEEN_SEC = 15000, '15с'
    '''Это модель банера новости'''
    state = models.BooleanField("Состояние", default=True)
    rotate_speed = models.IntegerField(choices=Speed.choices, default=5)


    class Meta:
        verbose_name = "Новостной баннер настроики"


class BannerNewsPromo(models.Model):
    '''Это доп модель банера новости'''
    url = models.URLField(null=True)
    image = models.ImageField(upload_to="img/banners/", null=True)
    promo = models.BooleanField(default=False)
    banner_news = models.ForeignKey(BannerNews,
                                    on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = "Новостной баннер"

class BannerUp(models.Model):
    class Speed(models.IntegerChoices):
        FIVE_SEC = 5000, '5с'
        TEN_SEC = 10000, '10с'
        FIFTEEN_SEC = 15000, '15с'
    '''Это модель банера новости'''
    state = models.BooleanField("Состояние", default=True)
    rotate_speed = models.IntegerField(choices=Speed.choices, default=5)


    class Meta:
        verbose_name = "Верхний баннер настроики"


class BannerMainUp(models.Model):
    '''Это доп модель банера сверху странички'''
    url = models.URLField("Ссылка", null=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="img/banners/", null=True)
    text = models.CharField(verbose_name="Описание баннера", max_length=100)
    banner_up = models.ForeignKey(BannerUp,
                                  on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Верхний баннер"


class BannerBackground(models.Model):
    '''Это модель банера фона'''
    imageBackground = models.ImageField("Картинка", default='back.jpg', upload_to='img/background/')
    color = models.CharField(max_length=7, default='')
    background = models.BooleanField("Состояние", default='')

    class Meta:
        verbose_name = "Фоновый баннер"
        verbose_name_plural = "Фоновые баннеры"

