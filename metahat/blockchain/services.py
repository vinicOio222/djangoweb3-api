from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from blockchain.models import Wallet
from config.settings import RPC_URL, BLOCK_SCAN

class Web3Service:
    def __init__(self):
        self.w3 = Web3(HTTPProvider(RPC_URL))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        if not self.w3.is_connected():
            raise Exception(f"Failed to connect to Ethereum node at {RPC_URL}")
    
    def create_ethereum_account(self, user):
        eth_account = self.w3.eth.account.create()
        wallet_instance = Wallet.objects.create(
            user=user,
            public_address=eth_account.address,
            private_key=eth_account.key.hex()
        )
        wallet_instance.save()
        return wallet_instance
    
    def get_balance(self, public_address):
        balance = self.w3.eth.get_balance(str(public_address))
        return balance
    
    def transfer(self, sender_address, sender_key, receiver_address, amount):
        sender_balance = self.get_balance(str(sender_address))
        amount_in_wei = self.w3.to_wei(amount, 'ether')

        gas_limit = 21000
        gas_price = self.w3.to_wei('50', 'gwei')

        if sender_balance < amount_in_wei:
            raise Exception(f"Insufficient funds from {sender_address} to transfer {amount} ETH to {receiver_address}")

        tx_object = {
            'from': str(sender_address),
            'to': str(receiver_address),
            'value': amount_in_wei,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'nonce': self.w3.eth.get_transaction_count(str(sender_address))
        }

        try:
            if sender_key.startswith('0x'):
                sender_key = sender_key[2:]
            sender_key_bytes = bytes.fromhex(sender_key)

            signed_tx = self.w3.eth.account.sign_transaction(tx_object, sender_key_bytes)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        except Exception as e:
            raise Exception(f"Failed to send transaction: {e}")

        return f"{BLOCK_SCAN}{tx_hash.hex()}"
