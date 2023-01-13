from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from banners.forms import BannersUpResumeForm, BannerBackgroundResumeForm, BannerNewsResumeForm, BannerMainUpFormSet, BannerNewsPromoFormSet
from banners.models import BannerMainUp, BannerBackground, BannerNewsPromo, BannerNews, BannerUp
from django.http import HttpResponse

# def delete_back(request, pk):
#     back = BannerBackground.objects.get(id=pk)
#     back.imageBackground.delete()
#     return redirect('banners')


# def delete_back(request, pk):
#     try:
#         back = BannerBackground.objects.get(id=pk)
#     except BannerBackground.DoesNotExist:
#         return redirect('banners')
#     if request.method == "GET":
#         back.delete()
#         return redirect('banners')
#     else:
#         return HttpResponse('Nonono!')


# def delete_up_img(request, pk):
#     try:
#         imgbup = BannerMainUp.objects.get(id=pk)
#     except BannerMainUp.DoesNotExist:
#         return redirect('banners')
#     if request.method == "GET":
#         imgbup.delete()
#         return redirect('banners')
#     else:
#         return HttpResponse('Nonono!')


def stat_view(request):
    return render(request, 'stat/index.html')

def check(user):
    return user.is_superuser

@user_passes_test(check, 'login_page')
def banners_view(request):
    obj_banner_news = get_object_or_404(BannerNews, id=1)
    obj_back_banner = get_object_or_404(BannerBackground, id=1)
    obj_banner_main = get_object_or_404(BannerUp, id=1)
    print(obj_banner_main)
    qs_main_banners = BannerMainUp.objects.filter(banner_up_id=1)
    print(qs_main_banners)
    qs_news_banners = BannerNewsPromo.objects.filter(banner_news_id=1)
    banner_main_form = BannersUpResumeForm(request.POST, request.FILES, instance=obj_banner_main)
    banner_back_form = BannerBackgroundResumeForm(request.POST, request.FILES, instance=obj_back_banner)
    banner_news_form = BannerNewsResumeForm(request.POST, request.FILES, instance=obj_banner_news)
    banner_main_up_formset = BannerMainUpFormSet(request.POST or None, request.FILES or None,
                                                 queryset=qs_main_banners, prefix="main")
    banner_news_promo_formset = BannerNewsPromoFormSet(request.POST or None, request.FILES or None,
                                                       queryset=qs_news_banners, prefix='news')

    if request.POST.get('type') == 'main_banner_form':
        print(request.POST)
        if banner_main_form.is_valid() and banner_main_up_formset.is_valid():
            print("Поехали дальше")
            banner_main = banner_main_form.save(commit=False)
            banner_up_main = banner_main_up_formset.save(commit=False)
            for del_item in banner_main_up_formset.deleted_objects:
                print(del_item)
                del_item.delete()
            for item in banner_up_main:
                item.banner_up = banner_main
                item.save()
            banner_main.save()
            print('Сохранили братуха')

            return redirect('banners')
        else:
            print(banner_main_up_formset.errors)
            print(banner_main_up_formset.non_form_errors())
            print("Чтото пошло под лед")
            return redirect('banners')

    if request.POST.get('type') == 'back_banner_form':
        # print(request.POST)
        if banner_back_form.is_valid():
            print(banner_back_form.cleaned_data)
            background_banner = banner_back_form.save(commit=False)
            if request.POST.get('background') == '1':
                background_banner.background = True
            else:
                background_banner.background = False

            # print(request.POST.get('background_banner'))
            if request.POST.get('background_banner') == 'delete':
                # background_banner.imageBackground = '/static/dist/img/empty-photo.png'
                background_banner.imageBackground ='/static/dist/img/white.png'
            background_banner.save()
            print("Огонь банер есть")
            return redirect('banners')
        else:
            print("Опять засада")

    if request.POST.get('type') == 'news_banner_form':
        print(request.POST)
        if banner_news_form.is_valid() and banner_news_promo_formset.is_valid():
            print("Поехали дальше")
            banner_news = banner_news_form.save(commit=False)
            banner_news_promo = banner_news_promo_formset.save(commit=False)

            for del_item in banner_news_promo_formset.deleted_objects:
                # print(del_item)
                del_item.delete()
            for item in banner_news_promo:
                item.banner_news = banner_news
                item.save()
            banner_news.save()
            print('Сохранили братуха')

            return redirect('banners')
        else:
            print(banner_news_promo_formset.errors)
            print(banner_news_promo_formset.non_form_errors())
            print("Всему пздец")
            return redirect('banners')

    else:
        banner_back_form = BannerBackgroundResumeForm(instance=obj_back_banner)
        banner_news_form = BannerNewsResumeForm(instance=obj_banner_news)
        banner_main_form = BannersUpResumeForm(instance=obj_banner_main)
        banner_main_up_formset = BannerMainUpFormSet(queryset=qs_main_banners, prefix="main")
        banner_news_promo_formset = BannerNewsPromoFormSet(queryset=qs_news_banners, prefix="news")
    context = {'banner_news_form': banner_news_form, 'banner_news_promo_formset': banner_news_promo_formset,
               'banner_back_form': banner_back_form, 'banner_main_form': banner_main_form,
               'banner_main_up_formset': banner_main_up_formset}
    return render(request, 'banners/banners.html', context)

