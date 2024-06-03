from web3 import AsyncWeb3
from web3.middleware import geth_poa_middleware
from blockchain.models import Wallet
from config.settings import RPC_URL

class Web3Service:
    def __init__(self):
        self.w3 = AsyncWeb3(AsyncWeb3.HTTPProvider(RPC_URL))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        if not self.w3.is_connected():
            raise Exception("Failed to connect to Ethereum node at {}".format(RPC_URL))
    
    def create_ethereum_account(self, user):
        eth_account = self.w3.eth.account.create()
        wallet_instance = Wallet.objects.create(
            user=user,
            public_address=eth_account.address,
            private_key=eth_account.key.hex()
        )
        wallet_instance.save()
        return wallet_instance
    
