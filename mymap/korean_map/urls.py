from . import views
from django.urls import path

urlpatterns = [
    path('seoul/', views.SeoulMap, name='서울시 지도')
]