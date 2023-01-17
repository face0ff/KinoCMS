from django import forms
from django.forms import ModelForm, CheckboxInput, NumberInput, FileInput, URLInput, TextInput, Select
from banners.models import BannerUp, BannerBackground, BannerNews, BannerMainUp, BannerNewsPromo
from django.forms import modelformset_factory


# ----------------------БаннерГлавный----------------------------
class BannersMainUpResumeForm(ModelForm):
    class Meta:
        model = BannerMainUp
        fields = ['image', 'url', 'text']

        widgets = {
            "image": FileInput(attrs={
                'class': 'custom-file',
                'style': 'display: none;',
                'onchange': 'download(this)'
            }),

            "url": URLInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ссылку",

            }),
            "text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите текст"
            })
        }


BannerMainUpFormSet = modelformset_factory(model=BannerMainUp, form=BannersMainUpResumeForm, extra=0, can_delete=True)


class BannersUpResumeForm(ModelForm):
    class Meta:
        model = BannerUp
        fields = ['state', 'rotate_speed']
        widgets = {
            "state": CheckboxInput(attrs={
                'class': 'custom-control-input',
                'id': 'customSwitch1'})}

    def __init__(self, *args, **kwargs):
        super(BannersUpResumeForm, self).__init__(*args, **kwargs)
        self.fields['rotate_speed'].required = False


# ----------------------БаннерФон----------------------------
class BannerBackgroundResumeForm(ModelForm):
    class Meta:
        model = BannerBackground
        fields = ['imageBackground', 'background', 'color']

        widgets = {
            "imageBackground": FileInput(attrs={
                'class': 'custom-file',
                'style': 'display: none;',
                'onchange': 'downloadBack(this)',
                'required': False
            }),
            "background": CheckboxInput(attrs={
                'class': 'custom-control-input',
                'id': 'check'
            }),
            'color': TextInput(attrs={

            })
        }


# ----------------------БаннерНовости----------------------------
class BannerNewsPromoResumeForm(ModelForm):
    # rotate_speed = forms.ModelChoiceField(queryset=BannerNews.objects.all(), required=False)

    class Meta:
        model = BannerNewsPromo
        fields = ['image', 'url', 'promo']

        widgets = {
            "image": FileInput(attrs={
                'class': 'form-control',
                'style': 'display: none',
                'onchange': 'download(this)'
            }),
            "url": URLInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ссылку"
            }),
            "promo": CheckboxInput(attrs={
                'class': 'form-control'
            })
        }
        # labels = {
        #     'image': '',
        #     'url': '',
        #     'promo': '',
        #
        # }

    # def __init__(self, *args, **kwargs):
    #     super(BannerNewsPromoResumeForm, self).__init__(*args, **kwargs)
    #     self.fields['delete'].widget = forms.HiddenInput()


BannerNewsPromoFormSet = modelformset_factory(model=BannerNewsPromo, form=BannerNewsPromoResumeForm, extra=0,
                                              can_delete=True)




class BannerNewsResumeForm(ModelForm):
    # rotate_speed = forms.IntegerField(required=False, widget=forms.Select)
    # rotate_speed = forms.ModelChoiceField(queryset=BannerNews.objects.all(), required=False)

    class Meta:
        model = BannerNews
        fields = ['state', 'rotate_speed']
        widgets = {
            "state": CheckboxInput(attrs={
                'class': 'custom-control-input',
                'id': 'customSwitch2'})}

    def __init__(self, *args, **kwargs):
        super(BannerNewsResumeForm, self).__init__(*args, **kwargs)
        self.fields['rotate_speed'].required = False
