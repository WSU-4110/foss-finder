from django.urls import path
from .views import category_view

urlpatterns = [
    path('categories/', views.categories, name='category_view'),


#category_view
