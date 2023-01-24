
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
        fields = ['name_ru',  'description_ru','name_uk',  'description_uk', 'condition_ru','condition_uk', 'logo',
                  'banner_up_image']
        widgets = {
            "name_ru": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите Название",
                'required': True
            }),
            "description_ru": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите Описание",
                'required': True
            }),
            "name_uk": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть назву",
                'required': True
            }),
            "description_uk": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введіть Опис",
                'required': True
            }),
            "condition_ru": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите Описание",
                'required': True
            }),
            "condition_uk": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введіть Опис",
                'required': True
            }),
            "logo": FileInput(attrs={
                'class': 'form-control',
                'style': 'opacity: 0;z-index: -1; position: absolute;',
                'onchange': 'download(this)',
                "title": "Добавьте картинку"

            }),
            "banner_up_image": FileInput(attrs={
                'class': 'form-control',
                'style': 'opacity: 0;z-index: -1; position: absolute;',
                'onchange': 'download(this)',
                "title": "Добавьте картинку"
            }),
        }


class FilmsForm(forms.ModelForm):

    gallery = GalleryForm()
    seo = SeoForm()

    class Meta:
        model = Film
        fields = ['title_ru','title_uk', 'description_ru', 'description_uk', 'release_date', 'main_image',
                  'trailer_url', 'type2d', 'type3d', 'typeIMAX']
        widgets = {
            "title_ru": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите Название",
                'required': True
            }),
            "description_ru": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите Описание",
                'required': True
            }),
            "title_uk": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть назву",
                'required': True
            }),
            "description_uk": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введіть Опис",
                'required': True
            }),

            "trailer_url": TextInput(attrs={
                'class': 'form-control',

                'placeholder': "Вставьте ссылку"
            }),
            "release_date": DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
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
        fields = ['number', 'description_ru', 'description_uk', 'create_date', 'banner_up_image',
                  'scheme', 'pk']
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите Номер",
                "required minlength": "1",
                "maxlength": "3",
                "pattern": "^\d+$",
                "title": "Введите число"
            }),
            "description_ru": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите Описание",
                'required': True
            }),
            "description_uk": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введіть Опис",
                'required': True
            }),

            "scheme": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            }),
            "create_date": DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
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
        fields = ['number', 'description_ru', 'description_uk',  'create_date', 'banner_up_image',
                  'scheme']
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите Номер",
                "required minlength": "1",
                "maxlength": "3",
                "pattern": "^\d+$",
                "title": "Введите число"

            }),
             "description_ru": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите Описание",
                'required': True
            }),
            "description_uk": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введіть Опис",
                'required': True
            }),

            "scheme": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            }),
            "create_date": DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Введите дату"
            }, format='%Y-%m-%d'),
            "banner_up_image": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            })}