from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.shortcuts import render
from users.models import User
from users.models import Session
import datetime
from django.contrib.auth.decorators import user_passes_test

def check(user):
    return user.is_superuser
# Create your views here.

@user_passes_test(check, 'login_page')
def stat_view(request):
    obj_users = User.objects.all()
    today = datetime.date.today()
    last_month = today.replace(month=today.month - 1)
    # print(last_month)

    sessions = Session.objects.annotate(dcount=Count('dateTime')).order_by('date').filter(date__gte=last_month)
    # print(sessions)
    sessions_days = []
    sessions_count = []
    for s in sessions:
        sessions_days.append(s.date.day)
    for s in sessions:
        int = sessions_days.count(s.date.day)
        sessions_count.append(int)
    users_gender_count = obj_users.values('gender').annotate(count=Count('gender'))
    print(sessions_days)
    print(sessions_count)
    context = {'obj_users': obj_users, 'sessions_count': sessions_count, 'sessions_days': sessions_days,
               'gender': users_gender_count}
    return render(request, 'adminLte/stat.html', context)


