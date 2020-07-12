from django.contrib import admin
from .models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ['No', 'Name', 'Father_name', 'Mother_name', 'Address', 'Contact']


admin.site.register(Client,ClientAdmin)
