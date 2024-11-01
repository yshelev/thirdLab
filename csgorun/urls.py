from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('cases/<str:name>/', views.case, name='case_page'),
    path('case_api/<str:name>/', views.case_api, name='case_page'),

    path('logout/', views.custom_logout, name='logout'),
]
