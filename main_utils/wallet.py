# lib
from bip32utils import BIP32Key


def get_wallet_from_xpub(xpub, no):
    return BIP32Key.fromExtendedKey(xpub).ChildKey(no).Address()
