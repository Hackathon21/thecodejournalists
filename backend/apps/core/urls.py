from django.urls import path
from .views import home_page

app_name = 'core'

urlpatterns = [
    path('', home_page, name='home'),
]
