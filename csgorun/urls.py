from django.urls import path
from . import views

app_name = 'csgorun'

urlpatterns = [
    path('', views.index, name='main_page'),

    path('profile/', views.profile, name='profile_page'),
    path('cases/<str:name>/', views.case, name='case_page'),
    path('open_case_api/<str:name>/', views.open_case_api, name='case_api'),
    path('sell_skins', views.sell_skins, name='sell_skins'),

    path('logout/', views.custom_logout, name='logout'),
]
