
from django import forms
from django.core.exceptions import ValidationError

from cinema.models import Cinema
from gallerySeo.forms import SeoForm, GalleryForm
from django.forms import Textarea, TextInput, DateInput, URLInput, FileInput, CheckboxInput, modelformset_factory
from .models import *


class NewsForm(forms.ModelForm):

    gallery = GalleryForm()
    seo = SeoForm()

    class Meta:
        model = NewsPromotions
        fields = ['name_ru', 'description_ru', 'name_uk', 'description_uk', 'main_image', 'video_url', 'date_publication', 'state', 'is_promotions']

        widgets = {
            "name_ru": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите Название",
                'required': 'True'
            }),
            "description_ru": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите Описание",
                'required': 'True'
            }),
            "name_uk": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть назву",
                'required': 'True'
            }),
            "description_uk": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введіть Опис",
                'required': 'True'
            }),
            "main_image": FileInput(attrs={
                'class': 'form-control',
                'style': 'opacity: 0;z-index: -1; position: absolute;',
                'onchange': 'download(this)'
            }),
            "video_url": URLInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ссылку"
            }),
            "date_publication": DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Введите дату"
            }, format='%Y-%m-%d'),
            "state": CheckboxInput(attrs={
                'class': 'form-control'
            }),
            "is_promotions": CheckboxInput(attrs={
                'class': 'form-control'
            })
        }


class PageForm(forms.ModelForm):

    gallery = GalleryForm()
    seo = SeoForm()

    class Meta:
        model = TemplatePage
        fields = ['name_ru', 'description_ru', 'name_uk', 'description_uk', 'main_image', 'state', 'main']

        widgets = {
            "name_ru": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите Название",
                'required': 'True'
            }),
            "description_ru": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите Описание",
                'required': 'True'
            }),
            "name_uk": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть назву",
                'required': 'True'
            }),
            "description_uk": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введіть Опис",
                'required': 'True'
            }),
            "main_image": FileInput(attrs={
                'class': 'form-control',
                'style': 'opacity: 0;z-index: -1; position: absolute;',
                'onchange': 'download(this)'
            }),
            "state": CheckboxInput(attrs={
                'class': 'form-control'
            }),
            "main": CheckboxInput(attrs={
                'class': 'form-control'
            }),
        }


class MainForm(forms.ModelForm):

    seo = SeoForm()

    class Meta:
        model = MainPage
        fields = ['phone', 'aditional_phone', 'seo_text', 'state']

        widgets = {
            "phone": TextInput(attrs={
                'type': "text",
                'class': 'form-control',
                'id': "phone-field",
                'name': "phone",
                'placeholder': "Номер телефона",
                'data-rule-required': "true",
                'data-rule-minlength': "10",
                'data-msg': "Введите номер телефона",
                'style': 'width:auto',
                "required minlength": "17",
                "pattern": "\+\d{2}\(\d{3}\)\d{3}-\d{4}",
                "maxlength": "17",
                "title": "Введить 12 цифр",
                'required': 'True'
            }),
            "aditional_phone": TextInput(attrs={
                'type':"text",
                'class':'form-control',
                'id':"phone-aditional_field",
                'name':"phone",
                'placeholder':"Номер телефона",
                'data-rule-required':"true",
                'data-rule-minlength':"10",
                'data-msg':"Введите номер телефона",
                'style': 'width:auto',
                "required minlength": "17",
                "pattern": "\+\d{2}\(\d{3}\)\d{3}-\d{4}",
                "maxlength": "17",
                "title": "Введить 12 цифр",
                'required': 'True'
            }),
            "seo_text": Textarea(attrs={
                'class': 'custom-file',
                'placeholder': "Seo text"
            }),
            "state": CheckboxInput(attrs={
                'class': 'form-control'
            }),

        }


class ContactForm(forms.ModelForm):

    seo = SeoForm()

    class Meta:
        model = Contacts
        fields = ['cinema_name', 'address', 'coordinate', 'state', 'logo']

        widgets = {
            "cinema_name": TextInput(attrs={
                'class': 'custom-file',
                'placeholder': "Введите название кинотеатра"
            }),
            "coordinate": TextInput(attrs={
                'class': 'custom-file',
                'placeholder': "Введите координаты",

            }),
            "address": Textarea(attrs={
                'class': 'custom-file',
                'placeholder': "Введите адресс",

            }),
            "state": CheckboxInput(attrs={
                'class': 'form-control'
            }),
            "logo": FileInput(attrs={
                'class': 'form-control',
                'style': 'opacity: 0;z-index: -1; position: absolute;',
                'onchange': 'download(this)'
            })
        }


ContactFormSet = modelformset_factory(Contacts, form=ContactForm, extra=0, can_delete=True)