from django.urls import path
#get our path modules in for the url map making
from rango import views
#import our views.py from rango app file

app_name= 'rango'

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
