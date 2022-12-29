from time import sleep
import redis
from celery import shared_task
from celery.result import AsyncResult
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse, HttpResponse




@shared_task()
def send_email_task(email_list, msg):
    client = redis.Redis(host='127.0.0.1')
    test = 1
    count = len(email_list)
    for i in email_list:
        send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, [i], html_message=msg)
        # percent = 100 // count
        # chislo = chislo + round(percent)
        # chislo = round(float(chislo), 1)
        # client.set('chislo', chislo)
        if test in range(1, count+1):
            chislo = round((test/count)*100)
            client.set('chislo', chislo)
            test= test+1








