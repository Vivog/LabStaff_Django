from django.shortcuts import render

def home(request):
    return render(request, 'main_app/main.html')

# Create your views here.
