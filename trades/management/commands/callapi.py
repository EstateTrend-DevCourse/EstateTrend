"""
custom command 구현 : https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/

"""


import logging

from django.core.management.base import BaseCommand
from trades.models import Region, RealEstate, RealEstateTrade
from trades.views import *


class Command(BaseCommand):
    help = "Call data from api."

    def handle(self, *args, **options):
        logging.info("Delete data from db")
        Region.objects.all().delete()
        RealEstate.objects.all().delete()
        RealEstateTrade.objects.all().delete()

        logging.info("Run python program that call API to get data")

        self.stdout.write(self.style.SUCCESS("Successfully loaded data from API."))
