# Generated by Django 3.2.15 on 2022-10-24 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0035_auto_20221024_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannermainup',
            options={'verbose_name': 'Верхний баннер'},
        ),
        migrations.AlterModelOptions(
            name='bannernews',
            options={'verbose_name': 'Новостной баннер настроики'},
        ),
        migrations.AlterModelOptions(
            name='bannernewspromo',
            options={'verbose_name': 'Новостной баннер'},
        ),
        migrations.AlterModelOptions(
            name='bannerup',
            options={'verbose_name': 'Верхний баннер настроики'},
        ),
    ]
