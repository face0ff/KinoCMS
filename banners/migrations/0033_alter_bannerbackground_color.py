# Generated by Django 3.2.15 on 2022-10-22 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0032_bannerbackground_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerbackground',
            name='color',
            field=models.CharField(default=False, max_length=7),
        ),
    ]
