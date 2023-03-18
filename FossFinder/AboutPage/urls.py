from django.urls import path

from . import views

urlpatterns = [
     path("<int:pk>/", views.about, name="about"),
     path("", views.about, name="about"),
]
