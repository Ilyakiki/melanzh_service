from django.contrib import admin
from .models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['description','price']

admin.site.register(Service,ServiceAdmin)
