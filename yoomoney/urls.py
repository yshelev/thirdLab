from django.urls import path
from yoomoney.views import create_payment_view

app_name = 'yoomoney'

urlpatterns = [
    path('create_payment/<int:total>/', create_payment_view, name='create_payment'),
]