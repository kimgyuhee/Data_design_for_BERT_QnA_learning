from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country/', views.country, name='country'),
]
