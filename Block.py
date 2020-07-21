

from utils import * 


class Block(Printable):
    def __init__(self, origin_node, miner_node, signature, previous_hash, timestamp, data, proof):
        self.origin_node = origin_node
        self.miner_node = miner_node 
        self.signature = signature 
        self.previous_hash = previous_hash
        self.timestamp = timestamp 
        self.data = data 
        self.proof = proof 
