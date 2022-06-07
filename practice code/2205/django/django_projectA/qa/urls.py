from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('index/country', views.country, name='country'),
    path('index/profile.html', views.profile, name='profile'),
    path('index/quiz.html', views.quiz, name='quiz'),
]
