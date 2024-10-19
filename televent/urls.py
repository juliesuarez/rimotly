from django.urls import path
from .views import home,dashboard

urlpatterns = [
    path('', home, name='home'),  # This is the root URL
    path('home/', home, name='home'),  # This is for /home/
     path('dashboard/', dashboard, name='dashboard'),
]
