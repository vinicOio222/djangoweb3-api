from web3 import Web3, geth_poa_middleware

RPC_URL = 'https://sepolia.infura.io/v3/'


class Web3Service:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(RPC_URL))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
