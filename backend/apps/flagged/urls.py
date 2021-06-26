from django.urls import path
from .views import flagged_sites

app_name = 'flagged'

urlpatterns = [
    path('', flagged_sites, name='home'),
]
