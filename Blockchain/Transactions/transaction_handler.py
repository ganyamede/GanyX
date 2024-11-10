import re
from .interfaces import Service
from Blockchain.Storage import db
from Blockchain.Blocks.blockchain_core import Blockchain
from Blockchain.Accounts.address_balance import getAddressBalance    
from Blockchain.Wallet.mnemonic_address import getAddressInformation


class Transfer(Service):
    def __init__(self, transaction: dict) -> None:
        self.seedPhrase_sender = transaction['sender']
        self.address_sender = getAddressInformation(self.seedPhrase_sender).address
        self.address_receiver = transaction['receiver']
        self.amount = transaction['amount']

    def get_transaction(self):
        return str(self.address_sender), str(self.address_receiver), str(self.amount)

class TransferValidator(Transfer):
    """check for extra security"""
    def __init__(self, transaction: dict):
        super().__init__(transaction)
        self.balance = getAddressBalance(self.address_sender).fetch()

    def _is_valid_address(self):
        """address validity check"""
        if len(self.address_receiver) != 64 or not re.match(r'^[0-9a-fA-F]{64}$', self.address_receiver):
            return False
        return True

    def _has_sufficient_funds(self):
        """check for availability of funds"""
        if self.amount > self.balance:
            return False
        return True

    def validate(self) -> bool:
        if not self._is_valid_address():
            raise ValueError("Invalid address.")
        if not self._has_sufficient_funds():
            raise ValueError("Insufficient funds.")
        return True
    
class TransferAgree(TransferValidator):
    def __init__(self, transaction):
        super().__init__(transaction)

    """Signing the contract and sending"""
    def send(self) -> dict:
        if self.validate():
            
            blockchain = Blockchain()
            blockchain.add_new_transaction(self.get_transaction())
            blockchain.mine(difficulty=2)

            for i, block in enumerate(blockchain.chain):
                block_json = {
                    "block": i, 
                    "hash": block.hash,
                    "timestamp": block.timestamp,
                    "sender": self.address_sender,
                    "receiver": self.address_receiver,
                    "amount": self.amount
                }
            
            db.insert(block_json)

            return block_json