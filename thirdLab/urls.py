from django.contrib import admin
from django.urls import path, include
from csgorun import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', include('social_django.urls', namespace='social')),
    path('', include('csgorun.urls')),
]
