from django.db import models


# Create your models here.
class Region(models.Model):
    base_address = models.CharField(max_length=200)  # 지번
    dong_name = models.CharField(max_length=200, default="")  # 동이름
    region_code = models.IntegerField(default=0)  # 지번code


class RealEstate(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    estate_name = models.CharField(max_length=200)  # 아파트 이름
    exclusive_area = models.FloatField(default=0.0)  # 전용면적
    year_of_construction = models.IntegerField(default=2000)  # 건축년도
    floor = models.IntegerField(default=0)  # 층


class RealEstateTrade(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    trade_price = models.IntegerField(default=0)  # 거래 금액
    trade_year = models.IntegerField(default=2000)  # 거래 연도
    trade_month = models.IntegerField(default=1)  # 거래 월
    trade_day = models.IntegerField(default=1)  # 거래 일
