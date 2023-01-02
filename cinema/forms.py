
from django import forms
from django.core.exceptions import ValidationError
from cinema.views import *

from .models import Film, Cinema, Hall
from django.forms import modelformset_factory, Textarea, TextInput, DateInput, URLInput, FileInput
from gallerySeo.forms import SeoForm, GalleryForm


class CinemaForm(forms.ModelForm):

    gallery = GalleryForm()
    seo = SeoForm()

    class Meta:
        model = Cinema
        fields = ['name', 'description', 'condition', 'logo',
                  'banner_up_image']
        widgets = {
            "name": TextInput(attrs={
                'class': 'custom-file',
                'placeholder': "Введите Название"
            }),
            "description": Textarea(attrs={
                'class': 'custom-file',
                'placeholder': "Введите Описание"
            }),
            "condition": Textarea(attrs={
                'class': 'custom-file',
                'placeholder': "Введите Описание"
            }),
            "logo": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            }),
            "banner_up_image": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            }),
        }


class FilmsForm(forms.ModelForm):

    gallery = GalleryForm()
    seo = SeoForm()

    class Meta:
        model = Film
        fields = ['title', 'description', 'release_date', 'main_image',
                  'trailer_url', 'type2d', 'type3d', 'typeIMAX']
        widgets = {
            "title": TextInput(attrs={
                'class': 'custom-file',
                'placeholder': "Введите Название"
            }),
            "description": Textarea(attrs={
                'class': 'custom-file',
                'placeholder': "Введите Описание"
            }),

            "trailer_url": URLInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ссылку"
            }),
            "release_date": DateInput(attrs={
                'type': 'date',
                'placeholder': "Введите дату"
            }, format='%Y-%m-%d'),
            "main_image": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            }),
        }
        # labels = {
        #     'title': 'Название кина',
        #     'description': 'Описание кина',
        #     'trailer_url': 'Трейлер кина',
        #     'release_date': 'Дата релиза. Чего? Кина',
        #     'main_image': 'Постер кина',
        #
        # }


class HallForm1(forms.ModelForm):

    def clean(self):
        data = self.cleaned_data['number']
        datapk = self.cleaned_data['pk']
        hall_number = Hall.objects.filter(cinema_id=datapk)
        hall_filter = hall_number.filter(number=data)
        if hall_filter:
            raise ValidationError("Такой зал уже создан")
        else:
            data

    gallery = GalleryForm()
    seo = SeoForm()
    cinema = Cinema()
    pk = forms.IntegerField()

    class Meta:
        model = Hall
        fields = ['number', 'description', 'create_date', 'banner_up_image',
                  'scheme', 'pk']
        widgets = {
            "number": TextInput(attrs={
                'class': 'custom-file',
                'placeholder': "Введите Номер"
            }),
            "description": Textarea(attrs={
                'class': 'custom-file',
                'placeholder': "Введите Описание"
            }),

            "scheme": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            }),
            "create_date": DateInput(attrs={
                'type': 'date',
                'placeholder': "Введите дату"
            }, format='%Y-%m-%d'),
            "banner_up_image": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            })}


class HallForm(forms.ModelForm):


    gallery = GalleryForm()
    seo = SeoForm()
    cinema = Cinema()


    class Meta:
        model = Hall
        fields = ['number', 'description', 'create_date', 'banner_up_image',
                  'scheme']
        widgets = {
            "number": TextInput(attrs={
                'class': 'custom-file',
                'placeholder': "Введите Номер"
            }),
            "description": Textarea(attrs={
                'class': 'custom-file',
                'placeholder': "Введите Описание"
            }),

            "scheme": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            }),
            "create_date": DateInput(attrs={
                'type': 'date',
                'placeholder': "Введите дату"
            }, format='%Y-%m-%d'),
            "banner_up_image": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            })}