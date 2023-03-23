from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.bug_submit_detail, name="bug_submit_detail"),
    path("", views.bug_submit, name="bug_submit"),
]