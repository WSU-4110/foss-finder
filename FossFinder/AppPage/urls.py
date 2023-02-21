from django.urls import path
from . import views

urlpatterns = [
    path("", views.software_index, name="software_index"),
    path("<int:pk>/", views.software_detail, name="software_detail"),
]