from .address_transactions import getTransactions

class getAddressBalance:
    def __init__(self, address):
        self.address = address

    def fetch(self):
        transactions = getTransactions(self.address).fetch()
        balance = 0

        for transaction in transactions['receiver']:
            balance += transaction['amount']

        for transaction in transactions['sender']:
            balance -= transaction['amount']

        return balance