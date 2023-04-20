"""FossFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings  
from django.conf.urls.static import static  
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('AppPage/', include("AppPage.urls")),
    path('', include("AppPage.urls")),
    path('SoftwareSubmissionPage/', include("SoftwareSubmissionPage.urls")),
    #without webpage/ it will update the main page, with it the /webpage is where it is applied
    path('AboutPage/', include("AboutPage.urls")),
    path('ReportBugs/', include("bug_report.urls")),
    path('FOSSGUY2.png', RedirectView.as_view(url=staticfiles_storage.url('img/FOSSGUY2.png'))),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
