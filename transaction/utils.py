# python
from decimal import Decimal

# project
from main_utils.blockchain_utils import get_wallet_amount


def is_confirmed(tr):
    amount = get_wallet_amount(wallet=tr.wallet)
    return tr.amount_btc - Decimal('0.0001') < amount < tr.amount_btc + Decimal('0.0001')
