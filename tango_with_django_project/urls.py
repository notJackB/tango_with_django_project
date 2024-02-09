"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
#this imports the include ability which makes our modular building block links
from rango import views
#this links our rango views app to this urls file
from django.conf import settings
#get the settings .py file imported in to get access to static and media
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    #this adds the url mapping from the views of our app to our site
    path('rango/', include('rango.urls')),
    #this maps any urls stating with rango/ to be handled by our rango app
    #with this we need to make a urls bit in our rango app to handle this request
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
