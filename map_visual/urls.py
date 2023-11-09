from . import views
from django.urls import path

urlpatterns = [
    path("sido/", views.SidoMap, name="sido_map"),
    path("sido/<str:sido_name>/", views.SigugunMap, name="sigugun_map"),
    path("sido/<str:sido_name>/<str:sigugun_name>", views.DongMap, name="dong_map"),
]
