from django.contrib import admin
from django.urls import path
from . import views

app_name = 'event'
urlpatterns = [
   path('', views.index, name='index'),
   path('register/', views.register, name='register'),
   path('registered/', views.registered, name='registered'),
   path('welcome/', views.welcome, name='welcome'),
   path('<int:event_id>/liste/', views.liste, name='liste'),
]
