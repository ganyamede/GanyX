# import hashlib

# def generate_address_from_seed(seed_phrase):
#     seed_bytes = seed_phrase.encode('utf-8')
#     hash_object = hashlib.sha256(seed_bytes)
#     address_hash = hash_object.hexdigest()
    
#     address = address_hash
    
#     return address

# # Пример использования
# seed_phrase = "broom dwarf two warfare bounce smart lucky cruel arena axis diesel wisdom"
# address = generate_address_from_seed(seed_phrase)
# print(f"Сгенерированный адрес: {address}")


from bip_utils import Bip39SeedGenerator, Bip39MnemonicGenerator, Bip44, Bip44Coins
from bip_utils import Bip44Changes, Bip32Utils

# Генерация сид-фразы
mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)  # Генерируем 12-словную сид-фразу
print(f"Сид-фраза: {mnemonic}")
