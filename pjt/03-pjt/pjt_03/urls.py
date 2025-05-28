# pjt_03/urls.py
from django.contrib import admin
from django.urls import path, include
from finance import views  # finance 앱의 views 모듈 임포트

urlpatterns = [
    path('', views.home, name='home'),  # 루트 URL에 대해 home 뷰 연결
    path('admin/', admin.site.urls),
    path('finance/', include('finance.urls')),
]
