from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    regions = Region.objects.all()
    context = {"regions": regions}
    return render(request, "trades/main.html", context)


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
