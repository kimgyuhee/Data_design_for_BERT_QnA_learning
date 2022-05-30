from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('index/country.html', views.country, name='country'),
    path('main/profile.html', views.profile, name='profile'),
    path('main/quiz.html', views.quiz, name='quiz'),
]
