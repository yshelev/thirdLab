import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from yookassa import Configuration, Payment
from yoomoney.payment import create_payment
from .models import BalanceChange
from .services import add_amount_to_user_balance_and_save_site_user_model, accept_balance_change


def create_payment_view(request, total):
    data = {
        'user_id' : request.user.id,
        'total' : total,
    }
    confirmation_url = create_payment(data)
    return HttpResponseRedirect(confirmation_url)

def accept_payment(request, change_id):
    change = BalanceChange.objects.get(id=change_id)
    add_amount_to_user_balance_and_save_site_user_model(request.user, amount=change.amount_value)
    accept_balance_change(change)
    return HttpResponseRedirect('/')