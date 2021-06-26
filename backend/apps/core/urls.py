from django.urls import path
from .views import app_page, home_page

app_name = 'core'

urlpatterns = [
    path('', home_page, name='home'),
    path('daily/', app_page, name='daily'),
]
