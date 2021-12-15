from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import car
# Register your models here.
@admin.register(car)
class carAdmin(admin.ModelAdmin):
    list_display=['name','price','date_of_purchase']