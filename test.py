from Blockchain.Wallet.bip39_mnemonic import Mnemonic
from Blockchain.Transactions.transaction_handler import TransferAgree
from Blockchain.Accounts.address_transactions import getTransactions
from Blockchain.Accounts.address_balance import getAddressBalance

# Create wallet
# for i in range(10):
#     seed = Mnemonic().mnemonic
#     Address = getAddressInformation(seed).address
#     print(seed, Address)
    
# Connect wallet

json = {
    'sender': 'autumn ball license aim sleep marriage few hazard actress argue charge order',
    'receiver': '4293e28127439e057cc696c5347a3e7c8b6a7fa47c09e0237b47614fca4d5429',
    'amount': 1
}

# Send money 
balance = getAddressBalance(json['receiver'])
print(f'Balance before: {balance.fetch_balance()}')

transf = TransferAgree(json)
sendTrans = transf.send()
hashTrans = getTransactions().fetch_transactions(sendTrans['hash'])
print(hashTrans)

balance = getAddressBalance(json['receiver'])
print(f'Balance after: {balance.fetch_balance()}')

