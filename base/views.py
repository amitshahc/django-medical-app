from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')  # Assuming you have an index.html template in your templates directory
