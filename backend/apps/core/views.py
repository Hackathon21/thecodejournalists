from re import template
from django.shortcuts import redirect, render
from django.urls import reverse


def home_page(request):
    status = request.user.is_authenticated
    if status:
        return render(request=request, template_name='index.html')
    return render(request=request, template_name='home.html')
