from django.urls import path
from .views import index, index_2

urlpatterns = [
    path('', index),
    path('sec', index_2),
]
