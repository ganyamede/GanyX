from flask import Blueprint, jsonify, request
from Blockchain.Accounts import (
    address_transactions,
    address_balance,
    address_state, 
)

auth_bp = Blueprint('auth', __name__)

class BlockchainData:
    def __init__(self, args) -> None:
        self.CallManager = {
            'getTransactions': address_transactions.getTransactions,
            "getAddressBalance": address_balance.getAddressBalance,
            "getAddressState": address_state.getAddressState
        }

        if args in self.CallManager:
            self.Manager = self.CallManager[args]


@auth_bp.route('/<action>/', methods=['POST'])
def profile(action):

    search_hash = 'hash' in request.form
    address = None
    if search_hash and action == 'getTransactions':
        if 'address' in request.form:
            address = request.form["address"]

        result = str(BlockchainData(action).Manager(address).fetch(request.form['hash']))
    else:
        result = str(BlockchainData(action).Manager(request.form['args']).fetch())

    return jsonify(
        {
            'result': result
        }
    )