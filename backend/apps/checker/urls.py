from django.urls import path
from .views import news_checker

app_name = 'checker'

urlpatterns = [
    path('', news_checker, name='home'),
]
