# Generated by Django 3.2.15 on 2022-10-16 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0023_remove_bannernewspromo_imageb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannermainup',
            name='banner_up',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='banners.bannerup'),
        ),
        migrations.AlterField(
            model_name='bannernewspromo',
            name='banner_news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='banners.bannernews'),
        ),
    ]
