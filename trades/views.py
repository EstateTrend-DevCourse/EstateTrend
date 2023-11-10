from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from datetime import datetime
from utils.local_name import *
from utils.local_name_dong import local_name_3
from map_visual.views import *


# Create your views here.
def index(request):
    # regions = Region.objects.all()
    raw_data = {
        "trading_volume": [],
        "average_price": [],
        "highest_price": [],
        "lowest_price": [],
    }
    context = {}

    if "gugun_nm" in request.GET:
        sido_nm = request.GET["sido_nm"]
        gugun_nm = request.GET["gugun_nm"]
        sub_regions = local_name_3[f"{sido_nm} {gugun_nm}"]
        context["sido"] = sido_nm
        context["gugun"] = gugun_nm

        trades = _get_gugun_trades(2023, 9, sido_nm, gugun_nm)
        raw_data["dong_nm"] = []
        for dong_nm in sub_regions:
            raw_data["dong_nm"].append(dong_nm)
            _context = _get_context(
                trades.filter(real_estate__region__dong_name=dong_nm)
            )
            raw_data = {
                key: value + [_context[key]] if key in _context else value
                for key, value in raw_data.items()
            }
        context["map"] = DongMap(sido_nm, gugun_nm, raw_data)
    elif "sido_nm" in request.GET:
        sido_nm = request.GET["sido_nm"]
        sub_regions = local_name_2[sido_nm]
        context["sido"] = sido_nm

        trades = _get_sido_trades(2023, 9, sido_nm)
        raw_data["sgg_nm"] = []
        for gugun_nm in sub_regions:
            raw_data["sgg_nm"].append(gugun_nm.replace(" ", ""))
            _context = _get_context(
                trades.filter(real_estate__region__gu_gun_name=gugun_nm)
            )
            raw_data = {
                key: value + [_context[key]] if key in _context else value
                for key, value in raw_data.items()
            }
        context["map"] = SigugunMap(sido_nm, raw_data)

    else:
        sub_regions = local_name_1["전국"]

        trades = _get_all_trades(2023, 9)
        raw_data["sidonm"] = []
        for sido_nm in sub_regions:
            raw_data["sidonm"].append(sido_nm)
            _context = _get_context(
                trades.filter(real_estate__region__si_do_name=sido_nm)
            )
            raw_data = {
                key: value + [_context[key]] if key in _context else value
                for key, value in raw_data.items()
            }
        context["map"] = SidoMap(raw_data)

    context.update(_get_context(trades))
    context["regions"] = sub_regions
    return render(request, "trades/index.html", context)


def _get_all_trades(cur_year, cur_month):
    monthly_trades = RealEstateTrade.objects.filter(
        trade_year=cur_year,
        trade_month=cur_month,
    )
    return monthly_trades


def _get_sido_trades(cur_year, cur_month, sido_nm):
    monthly_trades = RealEstateTrade.objects.filter(
        trade_year=cur_year,
        trade_month=cur_month,
        real_estate__region__si_do_name=sido_nm,
    )
    return monthly_trades


def _get_gugun_trades(cur_year, cur_month, sido_nm, gugun_nm):
    monthly_trades = RealEstateTrade.objects.filter(
        trade_year=cur_year,
        trade_month=cur_month,
        real_estate__region__si_do_name=sido_nm,
        real_estate__region__gu_gun_name=gugun_nm,
    )
    return monthly_trades


def _get_dong_trades(cur_year, cur_month, sido_nm, gugun_nm, dong_nm):
    monthly_trades = RealEstateTrade.objects.filter(
        trade_year=cur_year,
        trade_month=cur_month,
        real_estate__region__si_do_name=sido_nm,
        real_estate__region__gu_gun_name=gugun_nm,
        real_estate__region__dong_name=dong_nm,
    )
    return monthly_trades


def _get_context(trades):
    average_price, highest_price, lowest_price = 0, 0, 0
    trading_volume = trades.count()
    total_price = trades.aggregate(total_price=models.Sum("trade_price"))["total_price"]
    if trading_volume > 0:
        average_price = total_price / trading_volume

    trades = trades.order_by("trade_price")

    highest_price_trade = trades.last()
    if highest_price_trade:
        highest_price = highest_price_trade.trade_price

    lowest_price_trade = trades.first()
    if lowest_price_trade:
        lowest_price = lowest_price_trade.trade_price

    return {
        "trading_volume": trading_volume,
        "average_price": int(average_price),
        "highest_price": highest_price,
        "lowest_price": lowest_price,
    }


def detail(request):
    names = request.GET["dong_nm"].strip().split("-")
    sido_nm = names[0]
    gugun_nm = names[1]
    dong_nm = names[2]
    region = Region.objects.filter(
        si_do_name=sido_nm, gu_gun_name=gugun_nm, dong_name=dong_nm
    ).first()
    if region:
        # realestates = region.realestates
        trades = _get_dong_trades(2023, 9, sido_nm, gugun_nm, dong_nm)
        context = _get_context(trades)
        context["region"] = region
        # context["realestates"] = realestates
        context["trades"] = trades
    else:
        context = {}
    return render(request, "trades/detail.html", context)
