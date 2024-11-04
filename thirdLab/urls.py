from django.contrib import admin
from django.urls import path, include
from csgorun import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('social_django.urls')),
    path('', include('csgorun.urls', namespace='csgorun')),
    path('', include('yoomoney.urls', namespace='yoomoney')),
]
