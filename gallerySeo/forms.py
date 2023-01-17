from django import forms
from django.forms import modelformset_factory, FileInput

from .models import *


class SeoForm(forms.ModelForm):
    seo_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    seo_title = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    seo_keywords = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    seo_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Seo
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

        widgets = {
            "image": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            }),
        }


ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'