from . import views
from django.urls import path

urlpatterns = [
    path('seoul/', views.SeoulMap, name='seoul-map'),
    path('korea/', views.KoreaMap, name='korea-map')
]