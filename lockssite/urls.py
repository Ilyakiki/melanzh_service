from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns=[
    path('catalog',views.catalog,name='catalog'),
    path('services',views.ListServices.as_view(),name='services'),
    path('',views.homepage,name='homepage'),

]