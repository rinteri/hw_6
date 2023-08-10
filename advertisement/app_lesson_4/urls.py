from django.urls import path
from .views import index, ind, hw

urlpatterns = [
    path('', index),
    path('start', ind),
    path('lesson_4', hw)
]