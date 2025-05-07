# finance/urls.py
from django.urls import path
from . import views

app_name = 'finance'
urlpatterns = [
    path('index/', views.index, name='index'),  # 댓글 목록 페이지
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'), # 댓글 삭제 URL
    path('search/', views.search, name='search')
]

