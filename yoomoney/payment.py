from importlib.metadata import metadata
from yoomoney.models import BalanceChange
from yookassa import Configuration, Payment
from .config import config

Configuration.account_id = config["shop_id"]
Configuration.secret_key = config["secret_key"]

def create_payment(data):

    change = BalanceChange.objects.create(
        user_id=data['user_id'],
        amount_value=data["total"],
        is_accepted=True,
    )

    payment = Payment.create({
        'amount': {
            'value': data['total'],
            'currency': 'RUB',
        },
        'payment_method_data': {
            'type': 'bank_card',
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': 'https://example.com',
        },
        'metadata': {
            'table_id': change.id,
            'user_id': data['user_id'],
        },
        'capture': True,
        'refundable': False,
        'description': 'Оплата на сумму ' + str(data['total']),
    })


    return payment.confirmation.confirmation_url