from django.shortcuts import render

# Create your views here.

def checker_view(request):
    return render(request, 'home.html')