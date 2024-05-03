import yookassa
from yookassa import Payment
import uuid
from dotenv import load_dotenv
import os

load_dotenv()
yookassa.Configuration.account_id = os.getenv('ACCOUNT_ID')
yookassa.Configuration.secret_key = os.getenv('SECRET_KEY')


def create(amount, chat_id):
    id_key = str(uuid.uuid4())
    payment = Payment.create({
        "amount": {
            'value': amount,
            'currency': "RUB"
        },
        'paymnet_method_data': {
            'type': 'bank_card'
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': 'https://t.me/cryptostats58_bot'
        },
        'capture': True,
        'metadata': {
            'chat_id': chat_id
        },
        'description': 'Премиум функционал'
    }, id_key)

    return payment.confirmation.confirmation_url, payment.id


def check(payment_id):
    payment = yookassa.Payment.find_one(payment_id)
    if payment.status == 'succeeded':
        return payment.metadata
    else:
        return False