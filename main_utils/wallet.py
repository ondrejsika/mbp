# lib
from bip32utils import BIP32Key


def get_wallet_from_xpub(xpub, no):
    return BIP32Key.fromExtendedKey(xpub).ChildKey(0).ChildKey(no).Address()
