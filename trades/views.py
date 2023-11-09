from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from datetime import datetime
from utils.local_name import *
from map_visual.views import _render_map


# Create your views here.
def index(request):
    # regions = Region.objects.all()

    if "sido_nm" in request.GET:
        sido_nm = request.GET["sido_nm"]  # url query에서 시/도 명 가져와서 저장
        region_sido = local_name_2[sido_nm]
        context = {"regions": region_sido, "sido": sido_nm}  # context로 넘김
        if "gugun_nm" in request.GET:
            gugun_nm = request.GET["gugun_nm"]

            return HttpResponse("sido_nm gugun_nm")

    else:
        region_all = local_name_1["전국"]
        context = {"regions": region_all}

    context["map"] = _render_map()
    return render(request, "trades/index.html", context)


def detail(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    si_do_name = region.si_do_name
    gu_gun_name = region.gu_gun_name
    dong_name = region.dong_name

    realestates = region.realestates.all()
    # 현재 날짜를 기준으로 이번 달 거래 objects를 가져옴
    current_year = datetime(2023, 9, 1).year
    current_month = datetime(2023, 9, 1).month
    this_month_trading = RealEstateTrade.objects.filter(
        trade_year=current_year,
        trade_month=current_month,
        real_estate__region__pk=region_id,
    )
    trading_volume = this_month_trading.count()  # 이번달 거래량
    print(
        f"{current_year} - {current_month} trading volume: {trading_volume} trades"
    )  # test code
    # 평균값 구하는 과정
    total_price = this_month_trading.aggregate(total_price=models.Sum("trade_price"))[
        "total_price"
    ]
    if trading_volume > 0:
        average_price = total_price / trading_volume
    else:
        average_price = 0
    print(
        f"{current_year} - {current_month} average trading price: {average_price}"
    )  # test code

    # 가장 높은 거래 가격을 가진 주택을 찾는 코드
    highest_price_trade = this_month_trading.order_by("-trade_price").first()
    if highest_price_trade is not None:
        highest_price = highest_price_trade.trade_price
        print(
            f"The highest priced housing in {si_do_name} {gu_gun_name} {dong_name}: {highest_price_trade.real_estate.estate_name}, Price: {highest_price}"
        )
    else:
        highest_price = 0
        print(f"No trade information found")

    # 가장 낮은 거래 가격을 가진 주택을 찾는 코드
    lowest_price_trade = this_month_trading.order_by("trade_price").first()
    if lowest_price_trade:
        lowest_price = lowest_price_trade.trade_price
        print(
            f"The lowest priced housing in {si_do_name} {gu_gun_name} {dong_name}: {lowest_price_trade.real_estate.estate_name}, Price: {lowest_price}"
        )
    else:
        lowest_price = 0
        print(f"No trade information found")

    context = {
        "trading_volume": trading_volume,
        "average_price": average_price,
        "region": region,
        "lowest_price": lowest_price,
        "highest_price": highest_price,
        "realestates": realestates,
        "trades": this_month_trading,
    }
    return render(request, "trades/detail.html", context)
