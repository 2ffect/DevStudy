from django.contrib import admin
from django.urls import path, include
from contentfetch import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pjt04/', include('contentfetch.urls')),
    path('accounts/', include('accounts.urls')),
]
