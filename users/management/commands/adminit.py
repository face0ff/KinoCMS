from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = 'admin'
            email = 'admin@mail.com'
            password = '1542'
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_staff = True
            admin.is_superuser = True
            admin.save()
        else:
            print('Админа в студию')