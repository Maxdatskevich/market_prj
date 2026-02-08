from django.core.management.base import BaseCommand
from authapp.models import TravelUser
from authapp.models import TravelUserProfile


# Специальный класс-команда
class Command(BaseCommand):
    help = 'Update DB'

    def handle(self, *args, **options):
        # список с экз класса TravelUser
        users = TravelUser.objects.all()
        for user in users:
            users_profile = TravelUserProfile.objects.create(user=user)
            users_profile.save()


