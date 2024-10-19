import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .forms import VentFindingForm
from .models import VentFindings

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
