from .address_transactions import getTransactions

class getAddressState:
    def __init__(self, address):
        self.address = address

    def fetch(self):
        info = getTransactions(self.address)
        return {"state": bool(info.fetch()['sender'])}