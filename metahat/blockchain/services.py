from web3 import Web3
from web3.middleware import geth_poa
from ..blockchain.api.serializers import WalletSerializer

class Web3Service:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(geth_poa)
        if not self.w3.is_connected():
            raise Exception("Failed to connect to Ethereum node at {}".format(rpc_url))
    
    def create_ethereum_account(self, user):
        eth_account = self.w3.eth.account.create()
        wallet_instance = WalletSerializer(data={
            'user': user.id,
            'public_address': eth_account,
            'private_key': eth_account.privateKey.hex()
        })
        wallet_instance.is_valid(raise_exception=True)
        wallet_instance.save()
        return wallet_instance.data
