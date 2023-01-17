# Generated by Django 3.2.15 on 2023-01-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0017_alter_film_trailer_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Фильм'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Фильм'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Фильм'),
        ),
    ]