# Generated by Django 3.2.15 on 2022-10-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0013_auto_20221011_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerbackground',
            name='image',
            field=models.ImageField(null=True, upload_to='img/background/', verbose_name='Картинка'),
        ),
    ]
