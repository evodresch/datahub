from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.db import transaction
from .models import SPV, Location, Company
from .forms import SPVForm, LocationForm, CompanyForm
from django.http import HttpResponse


def landing_page(request):
    return render(request, 'spv_master_data/landing_page.html')


# View for a successful adding of an SPV
def success_page(request):
    return render(request, 'spv_master_data/success_page.html')

@transaction.atomic
def add_spv(request):
    if request.method == 'POST':
        spv_form = SPVForm(request.POST)
        location_form = LocationForm(request.POST)
        company_form = CompanyForm(request.POST)
        if spv_form.is_valid() and location_form.is_valid():
            # First, save the Location instance
            location_instance = location_form.save()
            # Save the Company instance
            company_instance = company_form.save()
            # Now, create an SPV instance but don't save it to the database yet
            spv_instance = spv_form.save(commit=False)
            # Link the newly created Location instance to the SPV instance
            spv_instance.location = location_instance
            # Link the newly created Company instance to the SPV instance
            spv_instance.company = company_instance
            # Finally, save the SPV instance to the database
            spv_instance.save()
            # Redirect to a new URL:
            return redirect('success_page')
    else:
        spv_form = SPVForm()
        location_form = LocationForm()
        company_form = CompanyForm()
    return render(request, 'spv_master_data/add_spv.html', {
        'spv_form': spv_form,
        'location_form': location_form,
        'company_form': company_form,})


# View that fetches the SPV data from the database and renders a template to display it
def spv_database_view(request):
    spvs = SPV.objects.all() # Fetch all instances
    return render(request, 'spv_master_data/spv_database.html', {'spvs': spvs})
