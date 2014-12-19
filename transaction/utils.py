# python
from decimal import Decimal

# project
from main_utils.blockchain import get_wallet_transaction


def is_confirmed(tr):
    txs = get_wallet_transaction(tr.wallet)
    for amount, wallet in txs:
        if tr.amount_btc - Decimal('0.0001') < amount < tr.amount_btc + Decimal('0.0001'):
            return True
    return False