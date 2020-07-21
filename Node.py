

from Wallet import Wallet
from BlockChain import BlockChain 

class Node():
    def __init__(self, network_info_dir):
        
        self.wallet_dir = None 
        self.chain_dir = None
        self.node_type = 'miner'
        self.network_info_dir = network_info_dir
        get_network_info(self.network_info_dir) 
        
        self.wallet = Wallet(wallet_dir) 
        self.blockchain = BlockChain(chain_dir)
    
    
    def get_network_info(self, network_info_dir):
        
        pass 