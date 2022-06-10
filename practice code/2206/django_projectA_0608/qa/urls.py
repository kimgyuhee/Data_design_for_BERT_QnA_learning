from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('mrc1/', views.mrc1, name='mrc1'),
]
