from django.contrib import admin
from .models import SPV, Location, Company

@admin.register(SPV)
class SPVAdmin(admin.ModelAdmin):
    list_display = ('projektgesellschaft', 'onesolar_id')  # Fields you want to show in the list view
    search_fields = ('onesolar_id',)  # Fields you want to be searchable

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('gemeinde', 'breitengrad', 'laengengrad')
    search_fields = ('gemeinde', 'breitengrad', 'laengengrad')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('handelsnummer', 'steuernummer')
    search_fields = ('handelsnummer', 'steuernummer')


