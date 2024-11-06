from importlib.metadata import metadata
from yoomoney.models import BalanceChange
from yookassa import Configuration, Payment
from .config import config
import uuid

Configuration.account_id = config["shop_id"]
Configuration.secret_key = config["secret_key"]

def create_payment(data):
    idempotency_key = str(uuid.uuid4())
    change = BalanceChange.objects.create(
        user_id=data['user_id'],
        amount_value=data["total"],
        is_accepted=False,
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
            'return_url':
                f'{config["ngrok_url"]}/accept_payment/'
                f'{change.id}',
        },
        'metadata': {
            'table_id': change.id,
            'user_id': data['user_id'],
        },
        # 'status': "waiting_for_capture",
        'capture': True,
        'refundable': False,
        'description': 'Оплата на сумму ' + str(data['total']),
    }, idempotency_key=idempotency_key)

    return payment.confirmation.confirmation_url