
class BlockChain():
    def __init__(self, chain_dir = None):
        self.chain = [] 
        self.chain_dir = chain_dir

        if self.chain_dir : load_chain(chain_dir)

        

    def load_chain(self, chain_dir) :

        try:
            with open(chain_dir, 'r') as file: 
                file_content = file.readlines() 
                self.chain = json.loads(file_content[0][:-1]) 

        except:
            print("couldn't load chain file")

            genesis_block = Block(0, '', [], 100, 0)
            self.chain = [genesis_block]