# Generated by Django 3.2.15 on 2022-10-12 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0019_alter_bannernewspromo_banner_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannernewspromo',
            name='banner_news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='banners.bannernews'),
        ),
    ]
