from django.urls import path
from .views import news_checker

app_name = 'api'

urlpatterns = [
    # path('posts/<int:pk>/', , name='posts_crud_page'),
    path('check-news/', news_checker, name='posts_list')
]
