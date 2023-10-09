from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Service
from .serializers import *
from .permitions import *
from rest_framework import generics


# Create your views here.

def homepage(request):
    # Представление главной страницы
    return render(request, 'lockssite/homepage.html')


def catalog(request):
    # Заглушка для будущего представления каталога
    return render(request, 'lockssite/catalog.html')


class ListServices(ListView):
    '''Список Услуг'''
    template_name = 'lockssite/services.html'
    model = Service
    context_object_name = 'Services'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


# Получение объектов
class ServiceAPIList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly,)


# Обновление объекта
class ServiceAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly,)


# Удаление объекта
class ServiceAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly,)
