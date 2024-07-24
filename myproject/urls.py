"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

#Root URL config
from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


def home_view(request):
    return HttpResponse("<h1>This is the home/h1>")
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path("crud/",include("crud.urls")),
    path("api/",include("api.urls")),
    path("", include("myapp.urls")),
    path("",home_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    

# URL Chaining
# It is the way to isolate urls in a large project.
#The main request always lands in root urls.py
#But the req can be forwarded 
