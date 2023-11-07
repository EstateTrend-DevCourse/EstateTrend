from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    regions = Region.objects.all()
    context = {"regions": regions}
    return render(request, "trades/index.html", context)


def detail(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    biggest_increase = "정자동"
    biggest_decrease = "상도동"
    context = {
        "region": region,
        "biggest_increase": biggest_increase,
        "biggest_decrease": biggest_decrease,
    }
    return render(request, "trades/detail.html", context)
