

from Wallet import Wallet
from BlockChain import BlockChain 

class Node():
    def __init__(self, wallet_dir= None, chain_dir = None, node_type = 'miner'):
        self.wallet = Wallet(wallet_dir) 
        self.blockchain = BlockChain(chain_dir)
        self.node_type = node_type 