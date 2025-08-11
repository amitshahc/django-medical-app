from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Assuming you have an index view in base/views.py
    # Add other URL patterns for your base app here
]