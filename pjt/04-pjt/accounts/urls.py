from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('deletd_stock/', views.delete_stock, name='delete_stock')
]
