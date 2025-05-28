from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:user_pk>/', views.profile, name='profile'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),

    # 구글 로그인 요청
    path('google/login/', views.google_login, name='google-login'),
    # 구글 로그인 인가 코드 수신 및 엑세스 토큰 요청
    path('google/callback/', views.google_callback, name='google-callback'),
]
