from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Service
# Create your views here.

def homepage(request):
    #Представление главной страницы
    return render(request, 'lockssite/homepage.html')

def catalog(request):
    #Заглушка для будущего представления каталога
    return render(request, 'lockssite/catalog.html')

class ListServices(ListView):
    '''Список Услуг'''
    template_name = 'lockssite/services.html'
    model = Service
    context_object_name = 'Services'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset