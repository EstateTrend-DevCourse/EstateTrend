from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from datetime import datetime


# Create your views here.
def index(request):
    regions = Region.objects.all()
    context = {"regions": regions}
    return render(request, "trades/main.html", context)


def detail(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    realestates = region.realestates.all()
    # 현재 날짜를 기준으로 이번 달 거래 objects를 가져옴
    current_year = datetime.now().year
    current_month = datetime.now().month
    this_month_trading = RealEstateTrade.objects.filter(
        trade_year=current_year, trade_month=current_month
    )
    trading_volume = this_month_trading.count()  # 이번달 거래량
    print(f"This month's trading volume: {trading_volume} trades")  # test code
    # 평균값 구하는 과정
    total_price = this_month_trading.aggregate(total_price=models.Sum("trade_price"))[
        "total_price"
    ]
    if trading_volume > 0:
        average_price = total_price / trading_volume
    else:
        average_price = 0
    print(f"This month's average trading price: {average_price}")  # test code
    si_do_name = region.si_do_name
    gu_gun_name = region.gu_gun_name
    dong_name = region.dong_name
    # 가장 높은 거래 가격을 가진 주택을 찾는 코드
    highest_price_housing = (
        RealEstate.objects.filter(region=region)
        .order_by("-realestatetrades__trade_price")
        .first()
    )
    if highest_price_housing:
        highest_price_trade = highest_price_housing.realestatetrades.first()
        if highest_price_trade:
            highest_price = highest_price_trade.trade_price
            print(
                f"The highest priced housing in {si_do_name} {gu_gun_name} {dong_name}: {highest_price_housing.estate_name}, Price: {highest_price}"
            )
        else:
            print(f"No trade information found for {highest_price_housing.estate_name}")
    else:
        print(f"No houses found in {si_do_name} {gu_gun_name} {dong_name}")
    # 가장 낮은 거래 가격을 가진 주택을 찾는 코드
    lowest_price_housing = (
        RealEstate.objects.filter(region=region)
        .order_by("realestatetrades__trade_price")
        .first()
    )
    if lowest_price_housing:
        lowest_price_trade = lowest_price_housing.realestatetrades.first()
        if lowest_price_trade:
            lowest_price = lowest_price_trade.trade_price
            print(
                f"The lowest priced housing in {si_do_name} {gu_gun_name} {dong_name}: {lowest_price_housing.estate_name}, Price: {lowest_price}"
            )
        else:
            print(f"No trade information found for {lowest_price_housing.estate_name}")
    else:
        print(f"No houses found in {si_do_name} {gu_gun_name} {dong_name}")
    # highest_price_housing = RealEstate.objects.filter(region=region).order_by('-real_estate_trade__trade_price').first()
    # if highest_price_housing:
    #     highest_price = highest_price_housing.real_estate_trade.trade_price
    #     print(f"The highest priced housing in {si_do_name} {gu_gun_name} {dong_name}: {highest_price_housing.estate_name}, Price: {highest_price}")
    # else:
    #     print(f"No houses found in {si_do_name} {gu_gun_name} {dong_name}")
    context = {
        "trading_volume": trading_volume,
        "average_price": average_price,
        "region": region,
        "lowest_price": lowest_price,
        "highest_price": highest_price,
        "realestates": realestates,
    }
    return render(request, "trades/index.html", context)
