import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from faker import Faker
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from banners.models import BannerMainUp, BannerUp, BannerNewsPromo, BannerNews, BannerBackground
from cinema.models import Film, Cinema, Hall
from gallerySeo.forms import SeoForm, ImageFormSet, GalleryForm
from gallerySeo.models import Image, Seo, Gallery
from users.forms import ChangeForm
from users.models import User, Session
from pages.forms import NewsForm, PageForm, MainForm, ContactForm, ContactFormSet
from pages.models import NewsPromotions, TemplatePage, MainPage, Contacts


def check(user):
    return user.is_superuser



@user_passes_test(check, 'login_page')
def news_view(request):
    news = NewsPromotions.objects.filter(is_promotions=False)
    context = {
        'news': news
    }
    return render(request, 'news/news.html', context)

@user_passes_test(check, 'login_page')
def news_create(request):
    if request.POST.get('type') == 'news_create_form':
        # print(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        news_form = NewsForm(request.POST, request.FILES)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none(), prefix='img')

        if news_form.is_valid() and seo_form.is_valid() and image_formset.is_valid():
            print("Ну дальше")
            news = news_form.save(commit=False)
            seo = seo_form.save(commit=False)
            images = image_formset.save(commit=False)
            seo.save()
            news.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            for item in images:
                item.gallery = gallery
                item.save()
            news.gallery = gallery
            news.save()
            print('Сохранили братуха')
            return redirect('news')
        else:
            # print(image_formset.non_form_errors())
            # print(image_formset.errors)
            print(news_form.errors)
            # print(seo_form.errors)
            print("Не валидно")
    else:
        news_form = NewsForm()
        seo_form = SeoForm()
        image_formset = ImageFormSet(queryset=Image.objects.none(), prefix='img')

    context = {
        'news_form': news_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }
    return render(request, 'news/news_create.html', context)

@user_passes_test(check, 'login_page')
def news_delete(request, pk):
    news = NewsPromotions.objects.get(pk=pk)
    news.delete()
    return redirect('news')

@user_passes_test(check, 'login_page')
def news_update(request, pk):
    obj_news = get_object_or_404(NewsPromotions, pk=pk)
    gal_qs = Image.objects.filter(gallery=obj_news.gallery.pk)
    print(obj_news.gallery_id)

    if request.POST.get('type') == 'news_update_form':
        print(request.POST, request.FILES)
        seo_form = SeoForm(request.POST, instance=obj_news.seo)
        news_form = NewsForm(request.POST, request.FILES, instance=obj_news)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=gal_qs, prefix='img')

        if news_form.is_valid() and seo_form.is_valid() and image_formset.is_valid():
            print("Ну дальше")
            news = news_form.save(commit=False)
            seo = seo_form.save(commit=False)
            images = image_formset.save(commit=False)
            for del_item in image_formset.deleted_objects:
                print(del_item)
                del_item.delete()
            # if request.POST.get('page') == 'delete':
            #     # background_banner.imageBackground = '/static/dist/img/empty-photo.png'
            #     news.main_image.delete()
            seo.save()
            news.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()

            for item in images:
                if item.image:
                    item.gallery = news.gallery
                    item.save()

            news.save()
            print('Сохранили братуха')
            return redirect('news')
        else:
            # print(image_formset.non_form_errors())
            # print(image_formset.errors)
            print(news_form.errors)
            # print(seo_form.errors)
            print("Не валидно")
    else:
        news_form = NewsForm(instance=obj_news)
        seo_form = SeoForm(instance=obj_news.seo)
        image_formset = ImageFormSet(queryset=gal_qs, prefix='img')

    context = {
        'news_form': news_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }
    return render(request, 'news/news_update.html', context)

@user_passes_test(check, 'login_page')
def promotions_view(request):
    promotions = NewsPromotions.objects.filter(is_promotions=True)
    context = {
        'promotions': promotions
    }
    return render(request, 'promotion/promotions.html', context)

@user_passes_test(check, 'login_page')
def promotions_delete(request, pk):
    promo = NewsPromotions.objects.get(pk=pk)
    promo.delete()
    return redirect('promotions')

@user_passes_test(check, 'login_page')
def promotions_create(request):
    if request.POST.get('type') == 'promo_create_form':
        print(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        promo_form = NewsForm(request.POST, request.FILES)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none(), prefix='img')

        if promo_form.is_valid() and seo_form.is_valid() and image_formset.is_valid():
            print("Ну дальше")
            promo = promo_form.save(commit=False)
            seo = seo_form.save(commit=False)
            images = image_formset.save(commit=False)
            seo.save()
            promo.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            for item in images:
                item.gallery = gallery
                item.save()
            promo.gallery = gallery
            promo.is_promotions = True
            promo.save()
            print('Сохранили братуха')
            return redirect('promotions')
        else:
            # print(image_formset.non_form_errors())
            # print(image_formset.errors)
            print(promo_form.errors)
            # print(seo_form.errors)
            print("Не валидно")
    else:
        promo_form = NewsForm()
        seo_form = SeoForm()
        image_formset = ImageFormSet(queryset=Image.objects.none(), prefix='img')

    context = {
        'promo_form': promo_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }
    return render(request, 'promotion/promotions_create.html', context)

@user_passes_test(check, 'login_page')
def promotions_update(request, pk):
    obj_promo = get_object_or_404(NewsPromotions, pk=pk)
    gal_qs = Image.objects.filter(gallery=obj_promo.gallery.pk)

    if request.POST.get('type') == 'promo_update_form':
        print(request.POST, request.FILES)
        seo_form = SeoForm(request.POST, instance=obj_promo.seo)
        promo_form = NewsForm(request.POST, request.FILES, instance=obj_promo)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=gal_qs, prefix='img')

        if promo_form.is_valid() and seo_form.is_valid() and image_formset.is_valid():
            print("Ну дальше")
            promo = promo_form.save(commit=False)
            seo = seo_form.save(commit=False)
            images = image_formset.save(commit=False)
            for del_item in image_formset.deleted_objects:
                print(del_item)
                del_item.delete()
            # if request.POST.get('page') == 'delete':
            #     # background_banner.imageBackground = '/static/dist/img/empty-photo.png'
            #     promo.main_image.delete()
            seo.save()
            promo.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            for item in images:
                if item.image:
                    item.gallery = promo.gallery
                    item.save()

            promo.is_promotions = True
            promo.save()
            print('Сохранили братуха')
            return redirect('promotions')
        else:
            print("Не валидно")
    else:
        promo_form = NewsForm(instance=obj_promo)
        seo_form = SeoForm(instance=obj_promo.seo)
        image_formset = ImageFormSet(queryset=gal_qs, prefix='img')

    context = {
        'promo_form': promo_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }
    return render(request, 'promotion/promotions_update.html', context)

@user_passes_test(check, 'login_page')
def pages_view(request):
    main_page = MainPage.objects.all().first()
    contacts_page = Contacts.objects.all().first()
    other_pages = TemplatePage.objects.all().filter(main=False)
    main_pages = TemplatePage.objects.all().filter(main=True)

    context = {
        'contacts_page': contacts_page,
        'other_pages': other_pages,
        'main_pages': main_pages,
        'main_page': main_page
    }
    return render(request, 'pages/pages.html', context)

@user_passes_test(check, 'login_page')
def pages_delete(request, pk):
    pages = TemplatePage.objects.get(pk=pk)
    pages.delete()
    return redirect('pages')

@user_passes_test(check, 'login_page')
def pages_create(request):
    if request.POST.get('type') == 'pages_create_form':
        print(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        pages_form = PageForm(request.POST, request.FILES)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none(), prefix='img')

        if pages_form.is_valid() and seo_form.is_valid() and image_formset.is_valid():
            print("Ну дальше")
            pages = pages_form.save(commit=False)
            seo = seo_form.save(commit=False)
            images = image_formset.save(commit=False)
            seo.save()
            pages.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            # main_name = ['Главная страничка', 'О кинотеатре', 'Головна сторінка', 'Про кінотеатр']
            # print(pages_form.cleaned_data['name'])
            # if pages_form.cleaned_data['name'] in main_name:
            #     pages.main = True
            for item in images:
                item.gallery = gallery
                item.save()

            pages.gallery = gallery
            pages.save()
            print('Сохранили братуха')
            return redirect('pages')
        else:
            print("Не валидно")
    else:
        pages_form = PageForm()
        seo_form = SeoForm()
        image_formset = ImageFormSet(queryset=Image.objects.none(), prefix='img')

    context = {
        'pages_form': pages_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }
    return render(request, 'pages/pages_create.html', context)

@user_passes_test(check, 'login_page')
def pages_update(request, pk):
    obj_page = get_object_or_404(TemplatePage, id=pk)
    gallery_qs = Image.objects.filter(gallery=obj_page.gallery.pk)
    if request.POST.get('type') == 'pages_update_form':
        page_form = PageForm(request.POST, request.FILES or None, instance=obj_page)
        image_formset = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs, prefix='img')
        seo_form = SeoForm(request.POST, instance=obj_page.seo, prefix='seo')
        print(request.POST, request.FILES)
        if all([page_form.is_valid(), seo_form.is_valid(), image_formset.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            page = page_form.save(commit=False)
            images = image_formset.save(commit=False)
            page.seo = seo
            for del_image in image_formset.deleted_objects:
                print(del_image)
                del_image.delete()
            # if request.POST.get('page') == 'delete':
            #     page.main_image.delete()

            if pk in range(1, 7):
                page.main = True
            # main_name = ['О кинотеатре', 'Детская комната', 'Реклама', 'Vip-зал', 'Кафе-бар', 'Про кінотеатр', 'Дитяча кімната']
            # print(page_form.cleaned_data['name'])
            # if page_form.cleaned_data['name'] in main_name:
            #     page.main = True
            for image in images:
                if image.image:
                    image.gallery = page.gallery
                    image.save()
            page.save()
            print(request.POST, request.FILES)
            return redirect('pages')
        else:
            print(image_formset.non_form_errors())
            print(image_formset.errors)
            print(page_form.errors)
            print(seo_form.errors)
            print("Не валидно")
    else:
        image_formset = ImageFormSet(queryset=gallery_qs, prefix='img')
        page_form = PageForm(instance=obj_page)
        seo_form = SeoForm(instance=obj_page.seo, prefix='seo')

    context = {'page_form': page_form, 'image_formset': image_formset, 'seo_form': seo_form}
    return render(request, 'pages/pages_update.html', context)

@user_passes_test(check, 'login_page')
def main_update(request, pk):
    obj_page = get_object_or_404(MainPage, id=pk)
    if request.POST.get('type') == 'main_update_form':
        main_form = MainForm(request.POST, request.FILES or None, instance=obj_page)
        seo_form = SeoForm(request.POST, instance=obj_page.seo, prefix='seo')
        print(request.POST, request.FILES)
        if all([main_form.is_valid(), seo_form.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            main = main_form.save(commit=False)
            main.seo = seo
            main.save()
            print(request.POST, request.FILES)
            return redirect('pages')
        else:
            print(main_form.errors)
            print(seo_form.errors)
            print("Не валидно")
    else:
        main_form = MainForm(instance=obj_page)
        seo_form = SeoForm(instance=obj_page.seo, prefix='seo')

    context = {'main_form': main_form, 'seo_form': seo_form}
    return render(request, 'pages/main_update.html', context)

@user_passes_test(check, 'login_page')
def contacts_update(request):
    obj_contact = get_object_or_404(Contacts, id=1)
    qs_contacts = Contacts.objects.all()

    if request.POST.get('type') == 'contacts_update_form':
        contact_formset = ContactFormSet(request.POST or None, request.FILES or None,
                                         queryset=qs_contacts, prefix="img")
        seo_form = SeoForm(request.POST, instance=obj_contact.seo)
        # print(request.POST, request.FILES)
        if all([contact_formset.is_valid(), seo_form.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            for form in contact_formset:

                print(form.prefix)
                print(request.POST.get('delete_logo'))
                if request.POST.get('delete_logo') == form.prefix:
                    item = form.save(commit=False)
                    item.logo.delete()
                else:
                    print('2')
            contact = contact_formset.save(commit=False)
            for del_item in contact_formset.deleted_objects:
                if del_item.id == 1:
                    pass
                else:
                    del_item.delete()
            for item in contact:
                item.save()
            print('Сохранили братуха')
            return redirect('pages')
        else:
            print("Не валидно")

    else:
        contact_formset = ContactFormSet(queryset=qs_contacts, prefix="img")
        seo_form = SeoForm(instance=obj_contact.seo)

    context = {
        'contact_formset': contact_formset,
        'seo_form': seo_form
    }
    return render(request, 'pages/contacts_update.html', context)


def user_editing(request, pk):

    user_obj = get_object_or_404(User, pk=pk)
    user_form = ChangeForm(instance=user_obj)

    if request.POST.get('type') == 'users_editing':

        user_form = ChangeForm(request.POST, instance=user_obj)
        print(request.POST)
        if user_form.is_valid():
            print('Проехали')
            user_form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.info(request, 'Неверный логин или пароль')
            else:
                login(request, user)
                return redirect('kino_cms')
        else:

            print(user_form.non_field_errors())
            print(user_form.errors)
            print("Не валид")

    context= {
        'user_form': user_form
    }

    return render(request, 'pages/user_editing.html', context)


# def about_site(request):
#     about = get_object_or_404(TemplatePage, id=1)
#     if about.state == True:
#         images = Image.objects.filter(gallery_id=about.gallery_id)
#         return render(request, 'pages/about_site.html', {'about': about, 'images': images})
#     else:
#         return redirect('kino_cms')
#
#
# def bar_site(request):
#     bar = get_object_or_404(TemplatePage, id=3)
#     if bar.state == True:
#         images = Image.objects.filter(gallery_id=bar.gallery_id)
#         return render(request, 'pages/bar_site.html', {'bar': bar, 'images': images})
#     else:
#         return redirect('kino_cms')
#
#
# def apk_site(request):
#     apk = get_object_or_404(TemplatePage, id=4)
#     if apk.state == True:
#         images = Image.objects.filter(gallery_id=apk.gallery_id)
#         return render(request, 'pages/apk_site.html', {'apk': apk, 'images': images})
#     else:
#         return redirect('kino_cms')
#
# def vip_site(request):
#     vip = get_object_or_404(TemplatePage, id=5)
#     if vip.state == True:
#         images = Image.objects.filter(gallery_id=vip.gallery_id)
#         return render(request, 'pages/vip_site.html', {'vip': vip, 'images': images})
#     else:
#         return redirect('kino_cms')
#
#
# def advert_site(request):
#     advert = get_object_or_404(TemplatePage, id=2)
#     if advert.state == True:
#         images = Image.objects.filter(gallery_id=advert.gallery_id)
#         return render(request, 'pages/advert_site.html', {'advert': advert, 'images': images})
#     else:
#         return redirect('kino_cms')
#
#
# def kids_site(request):
#     kids = get_object_or_404(TemplatePage, id=6)
#     if kids.state == True:
#         images = Image.objects.filter(gallery_id=kids.gallery_id)
#         return render(request, 'pages/kids_site.html', {'kids': kids, 'images': images})
#     else:
#         return redirect('kino_cms')


def news_site(request):

    all_news = NewsPromotions.objects.filter(is_promotions=False, state=True)
    paginator = Paginator(all_news, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        news = paginator.page(paginator.num_pages)

    return render(request, 'pages/news_site.html', {'page': page, 'news': news})

def contacts_site(request):
    contacts = Contacts.objects.filter(state=True)
    contacts_list = []
    for i in contacts:
        try:
            x = i.coordinate.split(',')[0]
            y = i.coordinate.split(',')[1]
            z = float(x)-10
        except:
            x = 50
            y = 50
            z = 50
        data = {
            'name': i.cinema_name,
            'logo': i.logo,
            'address': i.address,
            'x': x,
            'y': y,
            'z': str(z)
        }
        contacts_list.append(data)


    return render(request, 'pages/contacts_site.html', {'contacts_list': contacts_list})



def info_pages(request, pk):
    info = get_object_or_404(TemplatePage, id=pk)
    print(info.state)

    if info.state == True:
        images = Image.objects.filter(gallery_id=info.gallery_id)
        return render(request, 'pages/info_pages.html', {'info': info, 'images': images})
    else:
        return redirect('kino_cms')




