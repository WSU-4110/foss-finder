from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.software_submit_detail, name="software_submit_detail"),
    path("", views.software_submit, name="software_submit"),
]