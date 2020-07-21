from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.hazmat.primitives.asymmetric import rsa

import Crypto.Random
import binascii
import os 

class Wallet():
	
    def __init__(self, key_dir= None):
        self.private_Key= None
        self.public_Key =None
        self.ser_private_key = None
        self.ser_public_key = None 
        self.PADDING = padding.PSS(mgf=padding.MGF1(hashes.SHA256()),  salt_length= padding.PSS.MAX_LENGTH)

        try: self.load_keys(key_dir)
        except: 
            print("wallet couldnot find keys. Generating them... ")
            self.generate_keys() 
            self.save_keys()

        
    def generate_keys(self):
        self.private_key = rsa.generate_private_key(65537,1024,default_backend())
        self.public_key = self.private_key.public_key() 

    def sign(self, message): 
        signed = self.private_key.sign(message, self.PADDING, hashes.SHA256())
        return signed 

    def verify(self, pub_key, signed, message): 
        try : 
            pub_key.verify(signed, message, self.PADDING, hashes.SHA256()) 
            return True
        except : return False 
        
    def serialize(self):
        if self.ser_private_key : return self.ser_private_key, self.ser_public_key

        self.ser_private_key = self.private_key.private_bytes(
            encoding = serialization.Encoding.PEM, 
            format = serialization.PrivateFormat.PKCS8,
            encryption_algorithm = serialization.NoEncryption()
        )
        self.ser_public_key = self.public_key.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return self.ser_private_key, self.ser_public_key

    def load_keys(self, key_dir = os.getcwd()):
        public_key_file = os.path.join(key_dir, 'public_key.pem')
        private_key_file = os.path.join(key_dir, 'private_key.pem')
        
        with open(public_key_file, 'rb') as file:
            self.public_key = serialization.load_pem_public_key(file.read(), backend= default_backend()) 
        with open(private_key_file, 'rb') as file:
            self.private_key = serialization.load_pem_private_key(file.read(),password=None, backend= default_backend()) 

    def save_keys(self, key_dir = os.getcwd()):
        self.serialize() 

        public_key_file = os.path.join(key_dir, 'public_key.pem')
        private_key_file = os.path.join(key_dir, 'private_key.pem')

        with open(public_key_file, 'wb') as file : file.write(self.ser_public_key) 
        with open(private_key_file, 'wb') as file : file.write(self.ser_private_key) 


if __name__ == "__main__":

    ''' generate and save keys
    w = Wallet() 
    w.generate_keys() 

    s = b"plain text"
    s2 = b"plain tex"

    signed = w.sign(s)
    verification_true = w.verify(w.public_key, signed, s)
    verification_false = w.verify(w.public_key, signed, s2)

    w.save_keys() 
    '''

    w2 = Wallet(key_dir = os.getcwd()) 
    pri, pub = w2.serialize() 
    print(pri) 
    print(pub) 
