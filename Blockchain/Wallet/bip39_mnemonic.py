from bip_utils import Bip39MnemonicGenerator

class Mnemonic:
    def __init__(self) -> None:
        self.mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)