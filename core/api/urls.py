from django.urls import path
from .views import favorite_api_view

urlpatterns = [
    path('favorite/<int:pk>', favorite_api_view, name='favorite')
]
