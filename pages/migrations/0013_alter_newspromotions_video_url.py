# Generated by Django 3.2.15 on 2023-01-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20221228_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspromotions',
            name='video_url',
            field=models.URLField(),
        ),
    ]
