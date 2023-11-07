from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    regions = ["서울", "부산"]
    context = {"regions": regions, "id": 1}
    return render(request, "trades/index.html", context)


def detail(request, id):
    region = "서울"
    biggest_increase = "정자동"
    biggest_decrease = "상도동"
    context = {
        "region": region,
        "biggest_increase": biggest_increase,
        "biggest_decrease": biggest_decrease,
    }
    return render(request, "trades/detail.html", context)
