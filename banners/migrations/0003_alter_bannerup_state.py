# Generated by Django 3.2.15 on 2022-10-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0002_rename_test_bannermainup_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerup',
            name='state',
            field=models.BooleanField(default=False, verbose_name='Состояние'),
        ),
    ]
