from django.urls import path
from . import views

app_name = "trades"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
]
