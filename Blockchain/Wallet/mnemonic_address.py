from bip_utils import Bip39MnemonicValidator, Bip39Languages
import hashlib

class checkValidMnemonic:
    def __init__(self, seedPhrase):
        self.phrase = seedPhrase

    def validate_mnemonic(self):
        try:
            Bip39MnemonicValidator(Bip39Languages.ENGLISH).Validate(self.phrase)
            return True
        except:
            return False

class getAddressInformation(checkValidMnemonic):
    def __init__(self, seed_phrase):
        super().__init__(seed_phrase)
        if not self.validate_mnemonic():
            raise ValueError('There is no secret phrase')

        self.seed_bytes = str(seed_phrase).encode('utf-8')
        self.hash_object = hashlib.sha256(self.seed_bytes)
        self.address_hash = self.hash_object.hexdigest()
        self.address = self.address_hash