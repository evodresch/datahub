from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from .models import SPV, Location
from .forms import SPVForm, LocationForm
from django.http import HttpResponse


def landing_page(request):
    return HttpResponse("Welcome to the DataHub Dashboard!")


# View for a successful adding of an SPV
def success_page(request):
    return HttpResponse("Success!")


def add_spv(request):
    if request.method == 'POST':
        spv_form = SPVForm(request.POST)
        location_form = LocationForm(request.POST)
        if spv_form.is_valid() and location_form.is_valid():
            # First, save the Location instance
            location_instance = location_form.save()
            # Now, create an SPV instance but don't save it to the database yet
            spv_instance = spv_form.save(commit=False)
            # Link the newly created Location instance to the SPV instance
            spv_instance.location = location_instance
            # Finally, save the SPV instance to the database
            spv_instance.save()
            # Redirect to a new URL:
            return redirect('success_page')
    else:
        spv_form = SPVForm()
        location_form = LocationForm()
    return render(request, 'spv_master_data/main.html', {'spv_form': spv_form,
                                                         'location_form': location_form})
