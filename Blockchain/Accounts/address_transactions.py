from Blockchain.Storage import db
from typing import Optional

class getTransactions:
    def __init__(self, address: str = None):
        self.address = address

    def fetch(self, hash: str = None) -> list:
        if hash: 
            hash_transactions = db.select({'hash': hash})
            return hash_transactions
        
        sender = db.select({'sender': self.address})
        receiver = db.select({'receiver': self.address})

        return {"sender": sender, "receiver": receiver}