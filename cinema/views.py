import datetime
import json

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q


from django.core.exceptions import ValidationError
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from faker import Faker


from banners.models import BannerNewsPromo, BannerUp, BannerMainUp, BannerNews
from cinema.forms import FilmsForm, CinemaForm, HallForm, HallForm1
from cinema.models import Film, Cinema, Hall
from gallerySeo.forms import ImageFormSet, SeoForm, GalleryForm
from gallerySeo.models import Image, Seo, Gallery
from pages.models import MainPage, NewsPromotions, TemplatePage
from users.models import Session, Tiket


def check(user):
    return user.is_superuser


@user_passes_test(check, 'login_page')
def films_view(request):
    films = Film.objects.all()
    curent_time = datetime.datetime.now()
    films_now = Film.objects.filter(release_date__lte=curent_time)
    films_soon = Film.objects.filter(release_date__gt=curent_time)
    print(films)

    context = {
        'films_soon': films_soon,
        'films_now': films_now,
        'films': films
    }

    return render(request, 'films/films.html', context)

@user_passes_test(check, 'login_page')
def film_update(request, pk):
    obj_films = get_object_or_404(Film, id=pk)
    obj_seo = get_object_or_404(Seo, pk=obj_films.seo.pk)
    print(obj_films.gallery_id)

    if request.POST.get('type') == 'films_update_form':

        films_form = FilmsForm(request.POST, request.FILES, instance=obj_films)
        seo_form = SeoForm(request.POST, instance=obj_seo)
        image_formset = ImageFormSet(request.POST, request.FILES,
                                     queryset=Image.objects.filter(gallery=obj_films.gallery_id), prefix='img')
        print(request.POST, request.FILES)

        if films_form.is_valid() and image_formset.is_valid() and seo_form.is_valid():
            print("Ну дальше")
            film = films_form.save(commit=False)
            video_id = films_form.cleaned_data['trailer_url']
            if video_id.split('/')[3] != 'embed':
                try:
                    split = video_id.split('v=')[1].split('&')[0]
                    url = f'https://www.youtube.com/embed/{split}'
                    film.trailer_url = url
                except:
                    messages.warning(request, 'Добавьте ссылку с youtube')
                    return redirect('film_update', pk)
            images = image_formset.save(commit=False)
            seo = seo_form.save(commit=False)
            for del_item in image_formset.deleted_objects:
                print(del_item)
                del_item.delete()
            if request.POST.get('films') == 'delete':
                # background_banner.imageBackground = '/static/dist/img/empty-photo.png'
                film.main_image.delete()
            seo.save()
            film.seo = seo
            for item in images:
                if item.image:
                    item.gallery = film.gallery
                    item.save()
            film.save()
            print('Сохранили братуха')

            return redirect('films')
        else:

            print(image_formset.non_form_errors())
            print(image_formset.errors)
            print(films_form.errors)
            print(seo_form.errors)
            print("Не валидно")
            messages.warning(request, 'Добавьте картинку')
            return redirect('film_update', pk)
    else:
        films_form = FilmsForm(instance=obj_films)
        seo_form = SeoForm(instance=obj_films.seo)
        image_formset = ImageFormSet(queryset=Image.objects.filter(gallery=obj_films.gallery.pk), prefix='img')

    context = {
        'films_form': films_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }

    return render(request, 'films/film_update.html', context)

@user_passes_test(check, 'login_page')
def film_create(request):
    if request.POST.get('type') == 'films_create_form':
        films_form = FilmsForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none(), prefix='img')
        print(request.POST, request.FILES)
        if films_form.is_valid() and image_formset.is_valid() and seo_form.is_valid():
            print("Ну дальше")
            film = films_form.save(commit=False)
            video_id = films_form.cleaned_data['trailer_url']
            if video_id.split('/')[3] != 'embed':
                try:
                    split = video_id.split('v=')[1].split('&')[0]
                    url = f'https://www.youtube.com/embed/{split}'
                    film.trailer_url = url
                except:
                    messages.warning(request, 'Добавьте ссылку с youtube')
                    return redirect('film_update')
            images = image_formset.save(commit=False)
            seo = seo_form.save(commit=False)
            seo.save()
            film.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()

            for item in images:
                item.gallery = gallery
                item.save()
            film.gallery = gallery
            film.save()
            print('Сохранили братуха')

            return redirect('films')
        else:

            print(image_formset.non_form_errors())
            print(image_formset.errors)
            print(films_form.errors)
            print(seo_form.errors)
            print("Не валидно")
            return redirect('films')
    else:
        films_form = FilmsForm()
        seo_form = SeoForm()
        image_formset = ImageFormSet(queryset=Image.objects.none(), prefix='img')

    context = {
        'films_form': films_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }

    return render(request, 'films/film_create.html', context)

@user_passes_test(check, 'login_page')
def cinemas(request):
    cinemas = Cinema.objects.all()
    print(cinemas)

    context = {
        'cinemas': cinemas
    }
    return render(request, 'cinema/cinema.html', context)


def cinema_delete(request, pk):
    cinema = Cinema.objects.get(pk=pk)
    cinema.delete()
    return redirect('cinemas')

@user_passes_test(check, 'login_page')
def cinema_create(request):
    if request.POST.get('type') == 'cinema_create_form':

        cinema_form = CinemaForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none(), prefix='img')
        print(request.POST, request.FILES)
        if cinema_form.is_valid() and image_formset.is_valid() and seo_form.is_valid():
            print("Ну дальше")
            cinema = cinema_form.save(commit=False)
            images = image_formset.save(commit=False)
            seo = seo_form.save(commit=False)
            seo.save()
            cinema.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()

            for item in images:
                item.gallery = gallery
                item.save()
            cinema.gallery = gallery
            cinema.save()
            print('Сохранили братуха')

            return redirect('cinemas')
        else:

            print(image_formset.non_form_errors())
            print(image_formset.errors)
            print(cinema_form.errors)
            print(seo_form.errors)
            print("Не валидно")
            return redirect('cinemas')
    else:
        cinema_form = CinemaForm()
        seo_form = SeoForm()
        image_formset = ImageFormSet(queryset=Image.objects.none(), prefix='img')

    context = {
        'cinema_form': cinema_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }

    return render(request, 'cinema/cinema_create.html', context)

@user_passes_test(check, 'login_page')
def cinema_update(request, pk):
    obj_cinema = get_object_or_404(Cinema, pk=pk)
    gal_qs = Image.objects.filter(gallery=obj_cinema.gallery.pk)
    hall_form = Hall.objects.filter(cinema=pk)

    print(obj_cinema.pk)
    print(obj_cinema.gallery.pk)

    if request.POST.get('type') == 'cinema_update_form':

        cinema_form = CinemaForm(request.POST, request.FILES, instance=obj_cinema)
        seo_form = SeoForm(request.POST, instance=obj_cinema.seo)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=gal_qs, prefix='img')

        print(request.POST, request.FILES)
        if cinema_form.is_valid() and image_formset.is_valid() and seo_form.is_valid():
            print("Ну дальше")
            cinema = cinema_form.save(commit=False)
            images = image_formset.save(commit=False)
            seo = seo_form.save(commit=False)
            for del_item in image_formset.deleted_objects:
                print(del_item)
                del_item.delete()
            if request.POST.get('delete_logo') == 'delete':
                # background_banner.imageBackground = '/static/dist/img/empty-photo.png'
                cinema.logo.delete()
            if request.POST.get('delete_banner') == 'delete':
                # background_banner.imageBackground = '/static/dist/img/empty-photo.png'
                cinema.banner_up_image.delete()
            seo.save()
            cinema.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()

            for item in images:
                if item.image:
                    item.gallery = cinema.gallery
                    item.save()

            cinema.save()
            print('Сохранили братуха')

            return redirect('cinemas')
        else:

            print(image_formset.non_form_errors())
            print(image_formset.errors)
            print(cinema_form.errors)
            print(seo_form.errors)
            print("Не валидно")
            return redirect('cinemas')
    else:
        cinema_form = CinemaForm(instance=obj_cinema)
        seo_form = SeoForm(instance=obj_cinema.seo)
        image_formset = ImageFormSet(queryset=gal_qs, prefix='img')

    context = {
        'cinema_form': cinema_form,
        'hall_form': hall_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }

    return render(request, 'cinema/cinema_update.html', context)

@user_passes_test(check, 'login_page')
def hall_create(request, pk):
    if request.POST.get('type') == 'hall_create_form':

        hall_form = HallForm1(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none(), prefix='img')
        # print(request.POST, request.FILES)
        if hall_form.is_valid() and image_formset.is_valid() and seo_form.is_valid():
            print("Ну дальше")
            hall = hall_form.save(commit=False)
            images = image_formset.save(commit=False)
            seo = seo_form.save(commit=False)
            seo.save()
            hall.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            hall.cinema = Cinema.objects.get(pk=pk)

            for item in images:
                item.gallery = gallery
                item.save()
            hall.gallery = gallery
            # -----------------ПроверкаЗалов----------------------------
            #             data = hall_form.cleaned_data['number']
            #             hall_number = Hall.objects.filter(number=data)
            #             x = []
            #             for i in hall_number:
            #                 x.append(i.cinema.id)
            #             print(x)
            #             if pk in x:
            #                 raise ValidationError("Такой зал уже создан")
            #             else:
            hall.save()
            print('Сохранили братуха')
            return redirect('cinema_update', pk)
        # -----------------ПроверкаЗалов----------------------------

        # return redirect('cinema_update', pk)
        else:

            print(image_formset.non_form_errors())
            print(image_formset.errors)
            print(hall_form.errors)
            print(seo_form.errors)
            print("Не валидно")
            return redirect('cinema_update', pk)
    else:

        hall_form = HallForm1(data={'pk': pk, 'number': '0'})
        seo_form = SeoForm()
        image_formset = ImageFormSet(queryset=Image.objects.none(), prefix='img')

    context = {
        'hall_form': hall_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }

    return render(request, 'hall/hall_create.html', context)

@user_passes_test(check, 'login_page')
def hall_update(request, pk):
    obj_hall = get_object_or_404(Hall, pk=pk)
    cinema_pk = get_object_or_404(Cinema, pk=obj_hall.cinema.id)
    gal_qs = Image.objects.filter(gallery=obj_hall.gallery.pk)

    if request.POST.get('type') == 'hall_update_form':

        hall_form = HallForm(request.POST, request.FILES, instance=obj_hall)
        seo_form = SeoForm(request.POST, instance=obj_hall.seo)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=gal_qs, prefix='img')
        print(request.POST, request.FILES)

        if hall_form.is_valid() and image_formset.is_valid() and seo_form.is_valid():
            print("Ну дальше")
            hall = hall_form.save(commit=False)
            images = image_formset.save(commit=False)
            seo = seo_form.save(commit=False)
            if request.POST.get('delete_logo') == 'delete':
                # background_banner.imageBackground = '/static/dist/img/empty-photo.png'
                hall.scheme.delete()
            if request.POST.get('delete_banner') == 'delete':
                # background_banner.imageBackground = '/static/dist/img/empty-photo.png'
                hall.banner_up_image.delete()
            seo.save()
            hall.seo = seo
            gallery = GalleryForm().save(commit=False)
            gallery.save()

            for item in images:
                if item.image:
                    item.gallery = hall.gallery
                    item.save()
            hall.save()
            print('Сохранили братуха')

            return redirect('cinema_update', cinema_pk.id)
        else:

            print(image_formset.non_form_errors())
            print(image_formset.errors)
            print(hall_form.errors)
            print(seo_form.errors)
            print("Не валидно")
            return redirect('cinema_update', cinema_pk.id)
    else:
        hall_form = HallForm(instance=obj_hall)
        seo_form = SeoForm(instance=obj_hall.seo)
        image_formset = ImageFormSet(queryset=gal_qs, prefix='img')

    context = {
        'hall_form': hall_form,
        'image_formset': image_formset,
        'seo_form': seo_form
    }

    return render(request, 'hall/hall_update.html', context)

@user_passes_test(check, 'login_page')
def hall_delete(request, pk):
    obj_hall = get_object_or_404(Hall, pk=pk)
    cinema_pk = get_object_or_404(Cinema, pk=obj_hall.cinema.id)
    hall = Hall.objects.get(pk=pk)
    hall.delete()
    return redirect('cinema_update', cinema_pk.id)


def poster(request, pk):
    curent_time = datetime.datetime.now()
    films_now = Film.objects.filter(release_date__lte=curent_time)
    films_soon = Film.objects.filter(release_date__gt=curent_time)
    context = {
        'films_now': films_now,
        'films_soon': films_soon
    }
    return render(request, 'site/poster.html', context)


def film_card(request, pk):
    film = get_object_or_404(Film, pk=pk)
    phone = get_object_or_404(MainPage, pk=1)
    select_cinema = Cinema.objects.all()
    session = Session.objects.filter(film_id=pk)
    data_film = {}
    faker = Faker()
    fake = Faker('ru_RU')
    data_film = {
        'year': faker.year(),
        'country': fake.country(),
        'director': faker.name(),
        'writer': faker.name(),
        'producer': faker.name(),
        'actor': faker.name(),
        'cinema': faker.name()
    }

    context = {
        'data_film': data_film,
        'session': session,
        'select_cinema': select_cinema,
        'film': film
    }
    return render(request, 'site/film_card.html', context)


def cinema_site(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas': cinemas
    }
    return render(request, 'site/cinema_site.html', context)


def cinema_card(request, pk):
    print(pk)
    cinemas = get_object_or_404(Cinema, pk=pk)
    date = datetime.date.today()
    hals = Hall.objects.filter(cinema_id=cinemas.pk).order_by('number')
    images = Image.objects.filter(gallery_id=cinemas.gallery_id)
    sessions = Session.objects.filter(hall__cinema_id=cinemas.pk, date=date).order_by('dateTime')[:6]

    context = {

        'sessions': sessions,
        'images': images,
        'hals': hals,
        'cinemas': cinemas
    }
    return render(request, 'site/cinema_card.html', context)


def hall_card(request, pk, pk_alt):
    hall = get_object_or_404(Hall, pk=pk_alt)
    date = datetime.date.today()
    images = Image.objects.filter(gallery_id=hall.gallery_id)
    sessions = Session.objects.filter(hall_id=pk_alt, date=date).order_by('dateTime')[:6]

    context = {
        'sessions': sessions,
        'images': images,
        'hall': hall,
    }
    return render(request, 'site/hall_card.html', context)



def show_session(request):
    cinema = request.POST.get('cinema')
    film = request.POST.get('film')
    kino_type = request.POST.get('kino_type')
    print(cinema)
    print(film)
    print(kino_type)

    date = datetime.date.today()
    next = []
    for i in range(0, 7):
        var = date + datetime.timedelta(days=i)
        next.append(str(var))
    session = Session.objects.filter(hall__cinema_id=cinema, date__in=next)
    film_session = session.filter(film_id=film).order_by('date').distinct('date')
    if kino_type == '1':
        session = film_session.filter(tIMAX=True).order_by('date')
        serialized_data = serialize("json", session)
        return JsonResponse({'data': serialized_data}, status=200)
    elif kino_type == '2':
        session = film_session.filter(t2d=True).order_by('date')
        serialized_data = serialize("json", session)
        return JsonResponse({'data': serialized_data}, status=200)
    elif kino_type == '3':
        session = film_session.filter(t3d=True).order_by('date')
        serialized_data = serialize("json", session)
        return JsonResponse({'data': serialized_data}, status=200)
    else:
        serialized_data = serialize("json", film_session)
        return JsonResponse({'data': serialized_data}, status=200)


def select_session(request):
    date = request.POST.get('date')
    hall = request.POST.get('hall')
    film = request.POST.get('film')
    kino_type = request.POST.get('kino_type')
    # print(date)
    # print(hall)
    # print(kino_type)
    session = Session.objects.filter(hall__id=hall, film_id=film)
    hall_session = session.filter(date=date).order_by('date')

    if kino_type == '1':
        session = hall_session.filter(tIMAX=True).order_by('date')
        serialized_data = serialize("json", session)
        return JsonResponse({'data_hall': serialized_data}, status=200)
    elif kino_type == '2':
        session = hall_session.filter(t2d=True).order_by('date')
        serialized_data = serialize("json", session)
        return JsonResponse({'data_hall': serialized_data}, status=200)
    elif kino_type == '3':
        session = hall_session.filter(t3d=True).order_by('date')
        serialized_data = serialize("json", session)
        return JsonResponse({'data_hall': serialized_data}, status=200)
    else:
        serialized_data = serialize("json", hall_session)
        return JsonResponse({'data_hall': serialized_data}, status=200)


def kino_cms(request):
    current_time = datetime.datetime.now()
    search_qr = request.GET.get('search','')
    if search_qr:

        films_now = Film.objects.filter(release_date__lte=current_time, title__icontains=search_qr)
        films_soon = Film.objects.filter(release_date__gt=current_time, title__icontains=search_qr)

    else:

        films_now = Film.objects.filter(release_date__lte=current_time)
        films_soon = Film.objects.filter(release_date__gt=current_time)
    banners_up = BannerMainUp.objects.all()
    banners_sec = get_object_or_404(BannerUp, pk=1)
    banners_new = BannerNewsPromo.objects.all()
    banners_new_sec = get_object_or_404(BannerNews, pk=1)
    phone = get_object_or_404(MainPage, pk=1)
    seo_text = get_object_or_404(Seo, pk=phone.seo_id)




    context = {

        'seo_text': seo_text,
        'banners_new': banners_new,
        'banners_new_sec': banners_new_sec,
        'banners_sec': banners_sec,
        'banners_up': banners_up,
        'films_soon': films_soon,
        'films_now': films_now,

    }

    return render(request, 'site/KinoCMS.html', context)


def sessions(request, pk='0'):
    date = datetime.date.today()
    week = date + datetime.timedelta(days=6)
    cinemas = Cinema.objects.all()
    films = Film.objects.all()
    sessions_all = Session.objects.all().order_by('date')
    date_all = sessions_all.filter(date__gte=date, date__lte=week).distinct("date")
    user = request.user.pk
    booking = Tiket.objects.filter(user_id=user)
    list_book = []
    for i in booking:
        list_book.append(i.session_id)
    list_book = list(set(list_book))
    print(list_book)


    context = {'date_all': date_all, 'cinemas':cinemas, 'films':films, 'list_book': list_book }
    return render(request, 'site/sessions.html', context)

def form_sessions(qs_session):
    list_all = []

    for el in qs_session:
        date = el.date
        session_id = el.pk
        film_one = Film.objects.filter(id=el.film_id).values('title')
        obg = list(film_one)
        hall_one = Hall.objects.filter(id=el.hall_id).values('number')
        obgh = list(hall_one)
        time = el.dateTime
        dict_all = {
            'date': date,
            'film_one': obg[0]['title'],
            'hall_one': obgh[0]['number'],
            'time': time,
            'session_id': session_id
        }
        list_all.append(dict_all)
    return list_all


def filter_session(request):

    id_cinema = request.GET.get('id_cinema')
    id_film = request.GET.get('id_film')
    id_date = request.GET.get('id_date')
    id_hall = request.GET.get('id_hall')
    print(id_hall)
    date = datetime.date.today()
    cinemas = Cinema.objects.all()
    films = Film.objects.all()

    next = date + datetime.timedelta(days=1)
    sessions_all = Session.objects.all().order_by('dateTime')
    date_all = sessions_all.distinct("date")

    filter={}
    if len(id_cinema.split('_')) > 1:
        id_cinema = id_cinema.split('_')[1]
        halls = Hall.objects.filter(cinema_id=id_cinema)
        filter['hall__cinema_id'] = id_cinema

    if len(id_film.split('_')) > 1:
        id_film = id_film.split('_')[1]
        filter['film_id'] = id_film
    if len(id_hall.split('_')) > 1:
        id_hall = id_hall.split('_')[1]
        filter['hall_id'] = id_hall
    if id_date != 'Дата':
        filter['date'] = id_date
    else:
        next=[]
        for i in range(0, 7):
            var = date + datetime.timedelta(days=i)
            next.append(str(var))
        filter['date__in'] = next
        entries = sessions_all.filter(**filter).order_by('date', 'dateTime')
        list_all = form_sessions(entries)

        return JsonResponse({'data': list_all}, status=200)




    entries = sessions_all.filter(**filter).order_by('date', 'dateTime')
    list_all = form_sessions(entries)

    return JsonResponse({'data': list_all}, status=200)





def filter_session_all(request):

    date = datetime.date.today()
    sessions_all = Session.objects.all().order_by('date')
    next = []
    for i in range(0, 7):
        var = date + datetime.timedelta(days=i)
        next.append(str(var))
    sessions_next = sessions_all.filter(date__in=next).order_by('date', 'dateTime')
    list_all = form_sessions(sessions_next)

    return JsonResponse({'data_all': list_all}, status=200)


def filter_film(request):
    if request.GET.get('id_film'):
        id_film = request.GET.get('id_film')
    else:
        id_film = request.GET.get('id_alt_film')
    date = datetime.date.today()
    sessions_all = Session.objects.filter(film_id=id_film).order_by('date')
    next = []
    for i in range(0, 7):
        var = date + datetime.timedelta(days=i)
        next.append(str(var))
    sessions_next = sessions_all.filter(date__in=next).order_by('date', 'dateTime')
    list_all = form_sessions(sessions_next)

    return JsonResponse({'film_data': list_all}, status=200)

def filter_cinema(request):
    id_cinema = request.GET.get('id_cinema')

    date = datetime.date.today()
    sessions_all = Session.objects.filter(hall__cinema_id=id_cinema).order_by('date')
    next = []
    for i in range(0, 7):
        var = date + datetime.timedelta(days=i)
        next.append(str(var))
    sessions_next = sessions_all.filter(date__in=next).order_by('date', 'dateTime')
    list_all = form_sessions(sessions_next)

    return JsonResponse({'cinema_data': list_all}, status=200)

def filter_hall(request):
    id_cinema = request.GET.get('id_cinema')
    print(id_cinema)
    if len(id_cinema.split('_')) > 1:
        halls_cinema = Hall.objects.filter(cinema_id=id_cinema.split('_')[1])
        halls_data = serialize("json", halls_cinema)
        return JsonResponse({'halls_data': halls_data}, status=200)
    else:
        halls_cinema = Hall.objects.all()
        halls_data = serialize("json", halls_cinema)
        return JsonResponse({'halls_data': halls_data}, status=200)

def booking(request, pk):
    print(pk)
    session = get_object_or_404(Session, pk=pk)
    film = get_object_or_404(Film, pk=session.film.pk)
    print(session.dateTime)

    dateTimeNow = datetime.datetime.now().time()
    dateNow = datetime.datetime.now().date()
    print(dateNow)

    hall = get_object_or_404(Hall, pk=session.hall.pk)


    context = {
        'dateNow': dateNow,
        'dateTimeNow': dateTimeNow,
        'session': session,
        'film': film,
        'hall': hall

    }
    return render(request, 'site/booking.html', context)


def list_booking(request):

    if request.POST:
        list_data = request.POST.get('list_data')
        instance_next = json.loads(list_data);

        for item in instance_next:
            id = item['id']
            row = item['row']
            place = item['place']
            price = item['price']
            user = request.user.pk
            session_id = item['session_id']
            if request.POST:
                tiket = Tiket()
                tiket.id = id
                tiket.row = row
                tiket.place = place
                tiket.price = price
                tiket.user_id = user
                tiket.session_id = session_id
                tiket.booking = True
                tiket.save()
    user = request.user.pk
    session = request.GET.get('session')
    all_user_tikets = Tiket.objects.filter(user_id=user, session_id=session)
    all_tikets = Tiket.objects.filter(session_id=session).exclude(user_id=user)
    tikets_user_data = serialize("json", all_user_tikets)
    tikets_data = serialize("json", all_tikets)
    return JsonResponse({'tikets_user_data': tikets_user_data, 'tikets_data': tikets_data}, status=200)


def promotions_site(request):
    promotions = NewsPromotions.objects.filter(is_promotions=True).filter(state=True)
    context = {
        'promotions': promotions
    }
    return render(request, 'site/promotions_site.html', context)

def promotion_site(request, pk):
    promotions = get_object_or_404(NewsPromotions, pk=pk)
    context = {
        'promotions': promotions
    }
    return render(request, 'site/promotion_site.html', context)

def del_booking(request):
    id_booking = request.GET.get('id_booking')
    del_booking = get_object_or_404(Tiket, id=id_booking)
    del_booking.delete()
    ok = 'ok'
    return HttpResponse()