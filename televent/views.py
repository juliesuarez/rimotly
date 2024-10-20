import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .forms import VentFindingForm
from .models import VentFindings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FarmerRegisterForm


# Get an instance of a logger
logger = logging.getLogger(__name__)

@require_http_methods(["GET", "POST"])
def home(request):
    logger.info(f"Received {request.method} request to home view")
    
    if request.method == "POST":
        logger.info("Processing POST request")
        form = VentFindingForm(request.POST)
        logger.debug(f"Form data: {request.POST}")
        
        if form.is_valid():
            logger.info("Form is valid, saving data")
            try:
                form.save()
                logger.info("Data saved successfully")
                return JsonResponse({'success': True})
            except Exception as e:
                logger.error(f"Error saving form data: {str(e)}")
                return JsonResponse({'success': False, 'errors': 'Server error occurred'})
        else:
            logger.warning("Form is invalid")
            logger.debug(f"Form errors: {form.errors}")
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        logger.info("Processing GET request")
        form = VentFindingForm()
    
    logger.info("Rendering vent.html template")
    return render(request, "vent.html", {'form': form})

def dashboard(request):
    findings = VentFindings.objects.all().order_by('-id')  # Order by latest submission
    return render(request, 'admin.html', {'findings': findings})


def register_farmer(request):
    if request.method == 'POST':
        form = FarmerRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the farmer's data to the database
            messages.success(request, 'Registration successful!')
            return redirect('farmer_register')  # Redirect to the same page or a success page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FarmerRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'register_farmer.html', context)

def vent(request):
    return render(request,'vent_persona.html')