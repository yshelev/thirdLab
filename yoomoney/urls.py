from django.urls import path
from yoomoney.views import create_payment_view, accept_payment

app_name = 'yoomoney'

urlpatterns = [
    path('create_payment/<int:total>/', create_payment_view, name='create_payment'),
    path('accept_payment/<int:change_id>', accept_payment, name='accept_payment'),
]