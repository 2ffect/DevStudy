from django.urls import path
from . import views
from django.views.generic.base import RedirectView

app_name = 'pjt04'
urlpatterns = [
    path('index/', views.stock_finder, name='stock_finder'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
    path('', RedirectView.as_view(pattern_name='pjt04:stock_finder')),
]
