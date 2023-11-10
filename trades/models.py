from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Region(models.Model):
    base_address = models.CharField(max_length=200)  # 지번
    si_do_name = models.CharField(max_length=200, default="")  # 시/도 이름
    gu_gun_name = models.CharField(max_length=200, default="")  # 구/군 이름
    dong_name = models.CharField(max_length=200, default="")  # 동이름
    region_code = models.IntegerField(default=0)  # 지번code

    def __str__(self):
        return f"{self.si_do_name} {self.gu_gun_name} {self.dong_name}"


class RealEstate(models.Model):
    region = models.ForeignKey(
        Region, related_name="realestates", on_delete=models.CASCADE
    )
    estate_name = models.CharField(max_length=200)  # 아파트 이름
    exclusive_area = models.FloatField(default=0.0)  # 전용면적
    year_of_construction = models.IntegerField(default=2000)  # 건축년도
    floor = models.IntegerField(default=0)  # 층

    def __str__(self):
        return f"{self.estate_name}apt {self.floor}층 {self.exclusive_area}평"


class RealEstateTrade(models.Model):
    real_estate = models.ForeignKey(
        RealEstate, related_name="realestatetrades", on_delete=models.CASCADE
    )
    trade_price = models.IntegerField(default=0)  # 거래 금액
    trade_year = models.IntegerField(default=2000)  # 거래 연도
    trade_month = models.IntegerField(default=1)  # 거래 월
    trade_day = models.IntegerField(default=1)  # 거래 일

    def __str__(self):
        return f"{self.trade_year}년 {self.trade_month}월 {self.trade_day}일 거래금액: {self.trade_price}"
