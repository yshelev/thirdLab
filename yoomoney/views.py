from django.http import HttpResponseRedirect
from yoomoney.payment import create_payment


def create_payment_view(request, total=1):
    data = {
        'user_id' : request.user.id,
        'total' : total,
    }
    confirmation_url = create_payment(data)
    return HttpResponseRedirect(confirmation_url)