# Generated by Django 3.2.15 on 2022-12-27 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0013_auto_20221228_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Примьера в мире'),
            preserve_default=False,
        ),
    ]
