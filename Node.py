

from Wallet import Wallet
from BlockChain import BlockChain 

import os 
import json

class Node():
    def __init__(self, network_info_dir = None):
        
        self.wallet_dir = None 
        self.chain_dir = None
        self.node_type = 'miner'
        self.network_info_path = os.path.join(network_info_dir, 'network_info.json') if network_info_dir else os.path.join(os.getcwd(), 'network_info.json')
        self.get_network_info(self.network_info_path) 
        
        self.wallet = Wallet(self.wallet_dir) 
        #self.blockchain = BlockChain(chain_dir)
    
    
    def get_network_info(self, network_info_path): 
        with open(network_info_path, 'r') as file : 
            info = json.loads(file.read())
        self.wallet_dir = info['node']['wallet_dir'] if info['node']['wallet_dir'] else os.getcwd() 
        self.chain_dir = info['node']['chain_dir'] if info['node']['chain_dir'] else os.getcwd() 
        self.node_type = info['node']['node_type']


n = Node() 