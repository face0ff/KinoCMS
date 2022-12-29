# Generated by Django 3.2.15 on 2022-10-10 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallerySeo', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='seo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='gallerySeo.seo'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='seo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='gallerySeo.seo'),
        ),
        migrations.AlterField(
            model_name='newspromotions',
            name='gallery',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='gallerySeo.gallery'),
        ),
        migrations.AlterField(
            model_name='newspromotions',
            name='seo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='gallerySeo.seo'),
        ),
        migrations.AlterField(
            model_name='templatepage',
            name='gallery',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='gallerySeo.gallery'),
        ),
        migrations.AlterField(
            model_name='templatepage',
            name='seo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='gallerySeo.seo'),
        ),
    ]
