from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todos_main'),
    path('create_todo/', views.create_todo, name='todos_craeate'),
    path('<work>/', views.detail, name='todos_work'),
]
