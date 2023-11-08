"""
custom command 구현 : https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/

"""


import logging

from django.core.management.base import BaseCommand
from trades.models import Region, RealEstate, RealEstateTrade
from utils.scraping import make_dict_result


class Command(BaseCommand):
    help = "Call data from api."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Remove data from db"))
        logging.info("Delete data from db")
        Region.objects.all().delete()
        RealEstate.objects.all().delete()
        RealEstateTrade.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Remove Successed."))
        logging.info("Run python program that call API to get data")

        make_dict_result()
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from API."))
