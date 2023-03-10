# Generated by Django 3.2.15 on 2022-12-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_session_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='t2d',
            field=models.BooleanField(default=False, verbose_name='2d'),
        ),
        migrations.AddField(
            model_name='session',
            name='t3d',
            field=models.BooleanField(default=False, verbose_name='3d'),
        ),
        migrations.AddField(
            model_name='session',
            name='tIMAX',
            field=models.BooleanField(default=False, verbose_name='IMAX'),
        ),
    ]
