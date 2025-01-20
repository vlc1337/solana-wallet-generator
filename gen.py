import base58
from solders.keypair import Keypair

amount = 1000000 # how much attempts to make
end = "ke" # adress ends with...
start = "" # adress starts with...
include = "" # adress includes...

with open("wallets.txt", 'w') as f:
    for x in range(amount):
        account = Keypair()
        public_key = str(account.pubkey())
        private_key = base58.b58encode(account.secret() + base58.b58decode(str(public_key))).decode('utf-8')
        if public_key.lower().startswith(start) and public_key.lower().endswith(end) and include in public_key.lower():
            f.write(f"{public_key}:{private_key}\n")
