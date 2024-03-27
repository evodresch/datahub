from django.shortcuts import render, redirect
from .forms import SPVForm, SPVLocationForm
from django.http import HttpResponse

def landing_page(request):
    return HttpResponse("Welcome to the DataHub Dashboard!")

def add_spv(request):
    if request.method == 'POST':
        form = SPVLocationForm(request.POST)
        if form.is_valid():
            # First, create and save the Location instance
            location = Location(
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude'],
                area=form.cleaned_data['area'],
                address=form.cleaned_data['address']
            )
            location.save()

            # Now, create the SPV instance and assign the location to it
            spv = form.save(commit=False)
            spv.location = location
            spv.save()

            return redirect('main')  # Redirect as appropriate
    else:
        form = SPVLocationForm()
    return render(request, 'spv_master_data/main.html', {'form': form})
