from django.urls import path
from .views import home,dashboard,register_farmer,vent

urlpatterns = [
    path('', home, name='home'),  # This is the root URL
    path('home/', home, name='home'),  # This is for /home/
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register_farmer, name='farmer_register'),
    path('vent/', vent, name='vent'),
]
