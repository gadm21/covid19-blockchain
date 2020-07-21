
import os 

class BlockChain():
    def __init__(self, chain_dir = None):
        self.chain = [] 

        if not chain_dir : chain_dir = os.getcwd() 
        self.chain_path = os.path.join(chain_dir, 'chain.json') 
        load_chain(self.chain_path)



    def load_chain(self, chain_path) :

        try:
            with open(chain_path, 'r') as file: 
                file_content = file.readlines() 
                self.chain = json.loads(file_content[0][:-1]) 

        except:
            print("couldn't load chain file")

            genesis_block = Block(0, '', [], 100, 0)
            self.chain = [genesis_block]