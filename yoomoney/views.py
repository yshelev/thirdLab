from django.http import HttpResponseRedirect
from yoomoney.payment import create_payment
from .services import add_amount_to_user_balance_and_save_site_user_model

def create_payment_view(request, total):
    data = {
        'user_id' : request.user.id,
        'total' : total,
    }
    confirmation_url = create_payment(data)
    add_amount_to_user_balance_and_save_site_user_model(request.user, total)
    return HttpResponseRedirect(confirmation_url)