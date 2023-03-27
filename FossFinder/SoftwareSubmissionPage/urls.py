from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("<int:pk>/", views.software_submit_detail, name="software_submit_detail"),
    path("", views.software_submit, name="software_submit"),
]


urlpatterns = [  #Here and below is for Assignment 4
    path('admin/', admin.site.urls),
    path('rate/<int:post_id>/<int:rating>/', views.rate),
    path('', views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)