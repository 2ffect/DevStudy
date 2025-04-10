from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
    path('<int:book_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:book_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
