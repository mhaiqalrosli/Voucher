from django.conf.urls import include, url 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
]
