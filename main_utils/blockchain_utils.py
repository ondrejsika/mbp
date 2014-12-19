# lib
from blockchain.blockexplorer import get_address


def get_wallet_amount(wallet):
    return get_address(wallet).total_received
