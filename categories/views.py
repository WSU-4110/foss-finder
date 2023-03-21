from django.shortcuts import render

from .repositories import CategoryRepository

def category_view(request):
    category_repository = CategoryRepository()
    categories = category_repository.get_categories()
    return render(request, 'base.html')

