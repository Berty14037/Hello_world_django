from django.contrib import admin
from django.urls import path
from .views import score_view


urlpatterns = [
    path('', score_view, name='score_form'),

    
]