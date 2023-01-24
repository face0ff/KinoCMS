from celery.result import AsyncResult
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
import redis

from KinoCMS.settings import env
from users.forms import ChangeForm, MailForm, CreationForm
from users.models import User, Mail
from django.utils import translation


from users.tasks import send_email_task
def check(user):
    return user.is_superuser




@user_passes_test(check, 'login_page')
def users_view(request):
    users = User.objects.exclude(is_superuser=True)

    context = {
        'users': users
    }

    return render(request, 'users/users.html', context)

@user_passes_test(check, 'login_page')
def users_delete(request, pk):
    users = User.objects.get(pk=pk)
    if not users.is_superuser:
        users.delete()
    else:
        print("нам этого не нужно")
    return redirect('users')


def create_user(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        print(request.POST)
        user_creation_form = CreationForm(request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save(commit=False)
            user.save()
            messages.info(request, 'Аккаун создан')
            return redirect('login_page')
        else:
            messages.info(request, 'Пароли не совпадают')
    else:
        user_creation_form = CreationForm()

    context = {'user_form': user_creation_form}
    return render(request, 'users/register.html', context)


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, 'Неверный логин или пароль')
        else:
            login(request, user)
            translation.activate(user.language)
            request.LANGUAGE_CODE = user.language
            return redirect('kino_cms')

    context = {}
    return render(request, 'users/login_page.html', context)

def logout_page(request):
    logout(request)
    return redirect('kino_cms')


@login_required()
def users_update(request, pk):

    user_obg = get_object_or_404(User, pk=pk)
    user_form = ChangeForm(instance=user_obg)

    if request.POST.get('type') == 'users_update':
        user_form = ChangeForm(request.POST, instance=user_obg)
        print(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            print('Проехали')
            user.save()
            # translation.activate(user.language)
            # request.LANGUAGE_CODE = user.language
            return redirect('users')
        else:

            print(user_form.non_field_errors())
            print(user_form.errors)
            print("Не валид")

    context= {
        'user_form': user_form
    }

    return render(request, 'users/users_update.html', context)

@user_passes_test(check, 'login_page')
def mail_delete(request, pk):
    obj_mail = get_object_or_404(Mail, pk=pk)
    obj_mail.delete()
    return redirect('mail')


client = redis.Redis(host='redis')


def show_percent(request):
    chislo = client.get('chislo')
    return HttpResponse(chislo)


count = 0
@user_passes_test(check, 'login_page')
def mail_view(request):
    users = User.objects.all()
    obj_mail = Mail.objects.all().order_by("-date_added")[:5]

    if request.POST:
        print(request.POST, request.FILES)
        mail_form = MailForm(request.POST, request.FILES)
        if mail_form.is_valid():
            print('validno')
            mail_form.save(commit=False)
            if request.POST.get('type') =='one_user':
                email_list = request.POST.getlist('user')
                print(email_list)
                global count
                count = count + len(email_list)
                if mail_form.cleaned_data['HtmlTemplate']:
                    mail_form.save()
                    name = mail_form.cleaned_data['HtmlTemplate']
                    print(f'file/mail/{name}')
                    try:
                        msg = render_to_string(f'file/mail/{name}')
                    except:
                        messages.info(request, 'Не валидные данные')
                        return redirect('mail')
                    send_email_task.delay(email_list, msg)
                elif request.POST.get('mail_pk'):
                    name = get_object_or_404(Mail, pk=request.POST.get('mail_pk'))
                    url = name.HtmlTemplate.name
                    print(url)
                    try:
                        msg = render_to_string(url)
                    except:
                        messages.info(request, 'Не валидные данные')
                        return redirect('mail')
                    task = send_email_task.delay(email_list, msg)

                else:
                    messages.info(request, 'Не валидные данные')
                    return redirect('mail')
            if request.POST.get('type') == 'all_user':
                all_users = User.objects.all()
                email_list = []
                for user in all_users:
                    email_list.append(user.email)
                count = count + len(email_list)
                if mail_form.cleaned_data['HtmlTemplate']:
                    mail_form.save()
                    name = mail_form.cleaned_data['HtmlTemplate']
                    try:
                        msg = render_to_string(f'file/mail/{name}')
                    except:
                        messages.info(request, 'Не валидные данные')
                        return redirect('mail')
                    send_email_task.delay(email_list, msg)
                elif request.POST.get('mail_pk'):
                    name = get_object_or_404(Mail, pk=request.POST.get('mail_pk'))
                    url = name.HtmlTemplate.name
                    try:
                        msg = render_to_string(url)
                    except:
                        messages.info(request, 'Не валидные данные')
                        return redirect('mail')
                    send_email_task.delay(email_list, msg)
                else:
                    messages.info(request, 'Не валидные данные')
                    return redirect('mail')

        else:
            print('ne validno')
            messages.info(request, 'Не валидные данные')
            return redirect('mail')

    mail_form = MailForm()
    context = {
        'mail_form': mail_form,
        'obj_mail': obj_mail,
        'users': users,
        'count': count,


    }

    return render(request, 'mail/mail.html', context)

# def test_html(test):
#
#     split = test.split('.')[-1]
#     if split == 'html':
#         return True
#     else:
#         return False