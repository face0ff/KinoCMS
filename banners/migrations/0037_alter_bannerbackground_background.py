# Generated by Django 3.2.15 on 2022-11-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0036_auto_20221024_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerbackground',
            name='background',
            field=models.BooleanField(default='dist/img/empty-photo.png', verbose_name='Состояние'),
        ),
    ]
