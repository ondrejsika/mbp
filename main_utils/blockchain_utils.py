# python
from decimal import Decimal

# lib
from blockchain.blockexplorer import get_address


def sat_to_btc(sat):
    return Decimal(str(sat / float(10**8)))


def get_wallet_amount(wallet):
    return sat_to_btc(get_address(wallet).total_received)

