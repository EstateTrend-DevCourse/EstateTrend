from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    regions = Region.objects.all()
    context = {"regions": regions}
    return render(request, "trades/index.html", context)


def detail(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    estates = region.realestate_set.all()
    biggest_increase = "정자동"
    biggest_decrease = "상도동"
    context = {
        "region": region,
        "biggest_increase": biggest_increase,
        "biggest_decrease": biggest_decrease,
        "estates": estates,
    }
    return render(request, "trades/detail.html", context)


def detail_trade(request, region_id, estate_id):
    region = get_object_or_404(Region, pk=region_id)
    estate = get_object_or_404(RealEstate, pk=estate_id)

    real_estate_trades = estate.realestatetrade_set.all()
    context = {
        "region": region,
        "estate": estate,
        "trades": real_estate_trades,
    }
    return render(request, "trades/detail-trade.html", context)


def save_region():
    regions = []

    # Save region information


def save_real_estates():
    # function for storing data into RealEstate model

    # get data from api
    realestates = []

    # save data to model
    for re in realestates:
        realestate = RealEstate(**re)
        # https://stackoverflow.com/questions/1571570/can-a-dictionary-be-passed-to-django-models-on-create
        realestate.full_clean()
        # https://docs.djangoproject.com/en/4.2/ref/models/instances/#validating-objects
        # TODO : add try-except field
        realestate.save()


def save_real_estate_trades():
    real_estate_trades = []
    # call function that get data from api

    for ret in real_estate_trades:
        # parse trade into 3 parts: region, realestate, trade
        #
        region_list = []
        region = Region(**region_list)

        real_estate_list = []
        real_estate = RealEstate(**real_estate_list)

        trade_list = []
        trade = RealEstateTrade(**trade_list)
