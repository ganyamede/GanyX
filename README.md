# GanyX
Almost a complete decentralized mini network, but blocks are stored in NoSQL (MongoDB) Due to the lack of resources, this is a mini blockchain with translations, a full-fledged API, etc.

### Components

1. **Accounts**: Handles functionality related to account states, balances, and transactions.
- `address_balance.py`: Tracks the wallet balance.
- `address_state.py`: Tracks the wallet state.
- `address_transactions.py`: Tracks the transaction, recipient, and sender.

2. **Blocks**: Manages the room logic.
- `blockchain_core.py`: Contains the core logic of the blocks in the room, creation, and validation.

3. **Storage**: Provides interfaces and configures data storage.
- `config.py`: Configuration parameters for the database.
- `database.py`: Provides data persistence.
- `interfaces.py`: ABC storage interfaces.

4. **Transactions**: Manages the transaction processing system.
- `transaction_handler.py`: Basic logic for handling transactions in blocks.

- `interfaces.py`: Configure interfaces for transactions.

5. **Wallet**: Provides wallet management and address generation functionality.

- `bip39_mnemonic.py`: Generates BIP39 mnemonic phrases for wallets.

- `mnemonic_address.py`: External address of wallets based on mnemonics.

6. **Server**: Routes API for interacting with the indicator via HTTP.

- `App/routes/blockchain_api.py`: API endpoints for hardware-related functions.

### Getting Started

#### Prerequisites

- Python 3.9+
- Virtual environment set up (optional but recommended)


## Install

1. Clone the repository:
   ```bash
   git clone https://github.com/ganyamede/GanyX.git
   ```
   ```bash
   cd GanyX
   ```
   
2. Install the required dependencies (e.g., using pip for Python):
   ```bash
   pip install -r requirements.txt
   ```

3. Running the API
  ```bash
    python3 main.py
  ````

# API

The server exposes a REST API for interacting with the blockchain. Below are the main endpoints and the parameters they accept:

1. Get Transactions
    - Retrieves transactions associated with a specific account or block hash.

    - Endpoint: ```POST /api/getTransactions/```
    - Parameters: ```address(optional): wallet address```
                  ```hash(optional):```.

2. Get Address Balance
    - Gets the balance of a specific account address.

    - Endpoint: ```POST /api/getAddressBalance/```
    - Parameters: ```address: wallet address.```

3. Get Address State
    - Returns the current state of a specific account address.

    - Endpoint: ```POST /api/getAddressState/```
    - Parameters: ```address: wallet address.```
