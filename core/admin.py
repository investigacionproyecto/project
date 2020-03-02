from django.contrib import admin

# Register your models here.
from .models import Item, Boleto

admin.site.register(Item)
admin.site.register(Boleto)