# Generated by Django 3.2.15 on 2022-10-11 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0012_alter_bannermainup_banner_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannermainup',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Описание баннера'),
        ),
        migrations.AlterField(
            model_name='bannernewspromo',
            name='banner_news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='banners.bannernews'),
        ),
    ]
