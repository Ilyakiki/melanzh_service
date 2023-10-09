from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns=[
    path('api/v1/service/',views.ServiceAPIList.as_view()),
    path('api/v1/service/<int:pk>/',views.ServiceAPIUpdate.as_view()),
    path('api/v1/service/delete/<int:pk>/',views.ServiceAPIDestroy.as_view()),
    path('catalog',views.catalog,name='catalog'),
    path('services',views.ListServices.as_view(),name='services'),
    path('',views.homepage,name='homepage'),

]