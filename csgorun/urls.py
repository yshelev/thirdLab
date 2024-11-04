from django.urls import path
from . import views

app_name = 'csgorun'

urlpatterns = [
    path('', views.index, name='main_page'),

    path('profile/', views.profile, name='profile_page'),
    path('cases/<str:name>/', views.case, name='case_page'),
    path('case_api/<str:name>/', views.case_api, name='case_api'),

    path('logout/', views.custom_logout, name='logout'),
]
