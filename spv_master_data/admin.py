from django.contrib import admin
from .models import SPV, Location  # Import your models here

@admin.register(SPV)
class SPVAdmin(admin.ModelAdmin):
    list_display = ('projektgesellschaft', 'onesolar_id')  # Fields you want to show in the list view
    search_fields = ('onesolar_id',)  # Fields you want to be searchable
    # You can add more options as needed

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('gemeinde', 'gemarkung', 'plz')
    search_fields = ('gemeinde', 'gemarkung', 'plz')
    # You can add more options as needed
