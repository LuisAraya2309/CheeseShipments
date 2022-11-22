'''
Instituto Tecnológico de Costa Rica
Escuela de Ingeniería en Computación
Criptografía
Autores:
Luis Carlos Araya Mata
Rolbin Méndez Brenes
Josue Gabriel Navarro Solís
'''

import datetime , hashlib , json
from auxiliarFunctions import *

 
class Blockchain:
    '''
    '''
    
    def __init__(self):
        '''
        Here we try to see if there is already a blockchain saved in the directory to load it.
        If not, we create the binary file.
        '''
        self.chain : list
        try:
            self.chain = loadChain()
            print('Found shipment trazability, loading it...\nReady to go')
        except:
            print('Creating new shipment trazability from scratch...\nReady to go')
            self.chain = []
            saveBlockChain([])
                
 
    def createBlock(self, proof : int, originalShipment, cheeseAmount : int, product : dict, buyer) -> dict:
        '''
        '''
        newBlock : dict = {
            
                    'index': len(self.chain) + 1,
                    'timestamp': str(datetime.datetime.now()),
                    'proof': proof,
                    'originalShipment': originalShipment,
                    'product' : product,
                    'cheeseAmount' : cheeseAmount,
                    'buyer' : buyer.__str__()
                
                 }
        
        self.chain.append(newBlock)
        saveBlockChain(self.chain)                
        return newBlock
       
    def getPreviousBlock(self):
        '''
        '''
        return self.chain[-1]
       
    
    def proofOfWork(self, previousProof):
        '''
        '''
        newProof = 1
        checkProof = False
         
        while checkProof is False:
            hashOperation = hashlib.sha256(
                str(newProof ** 2 - previousProof ** 2).encode()).hexdigest()
            if hashOperation[:5] == '00000':
                checkProof = True
            else:
                newProof += 1
                 
        return newProof
 
    def hash(self, block : dict):
        encodedBlock = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()
 
    def isChainValid(self, chain : list):
        previousBlock = chain[0]
        blockIndex = 1
         
        while blockIndex < len(chain):
            block = chain[blockIndex]
            if block['originalShipment'] != self.hash(previousBlock):
                print('This chain is not valid.')
                return False
               
            previousProof = previousBlock['proof']
            proof = block['proof']
            hashOperation = hashlib.sha256(
                str(proof**2 - previousProof**2).encode()).hexdigest()
             
            if hashOperation[:5] != '00000':
                return False
            previousBlock = block
            blockIndex += 1
            
        print('This chain is valid!')
        return True
    
    def __str__(self):
        
        for block in self.chain:
            print(block)
 