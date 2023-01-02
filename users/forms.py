from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import Textarea, TextInput, DateInput, URLInput, FileInput, CheckboxInput, modelformset_factory

from users.models import User, Mail


class CreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': "Retype password"}))


    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class ChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",
                                                             'style': 'width:auto', }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email",
                                                            'style': 'width:auto'}))
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'placeholder': "Password",
                                                                                  'style': 'width:auto'}))
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'placeholder': "Retype password",
                                                                                  'style': 'width:auto'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "First name",
                                                         'style': 'width:auto'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Last name",
                                                            'style': 'width:auto'}))
    birthday_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date',
                                                                  'placeholder': "Введите дату", 'style': 'width:auto'}, format='%Y-%m-%d'))

    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Address",
                                                            'style': 'width:auto'}))
    card_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Card Number",
                                                                'style': 'width:auto'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "City",
                                                         'style': 'width:auto'}))
    gender = forms.ChoiceField(choices=User.CHOISES_gender, widget=forms.RadioSelect())
    language = forms.ChoiceField(choices=User.CHOISES_language, widget=forms.RadioSelect())
    phone = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'class':'form-control', 'id':"phone-field",
                                                          'name':"phone", 'placeholder':"Номер телефона",
                                                          'data-rule-required':"true", 'data-rule-minlength':"10",
                                                          'data-msg':"Введите номер телефона", 'style': 'width:auto'}))

    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'birthday_date', 'address', 'card_number',
                  'city', 'gender', 'language', 'phone', 'email', 'username', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user_form = super().save(commit=False)
        user_form.set_password(self.cleaned_data["password1"])
        if commit:
            user_form.save()
        return user_form


class MailForm(forms.ModelForm):


    class Meta:
        model = Mail
        fields = '__all__'

        widgets = {

            "HtmlTemplate": FileInput(attrs={
                'style': 'display: none',
                'onchange': 'show_name(this)',
                'required': False
            })
        }


MailFormSet = modelformset_factory(model=Mail, form=MailForm, extra=0,
                                              can_delete=True)