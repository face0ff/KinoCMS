# Generated by Django 3.2.15 on 2022-10-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0017_alter_bannerbackground_imagebackground'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannernewspromo',
            name='promo',
            field=models.BooleanField(default=False, verbose_name='Акции'),
        ),
        migrations.AlterField(
            model_name='bannerbackground',
            name='background',
            field=models.BooleanField(default=False, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='bannernews',
            name='state',
            field=models.BooleanField(default=False, verbose_name='Состояние'),
        ),
    ]
