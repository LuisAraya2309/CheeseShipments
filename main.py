'''
Instituto Tecnológico de Costa Rica
Escuela de Ingeniería en Computación
Criptografía
Autores:
Luis Carlos Araya Mata
Rolbin Méndez Brenes
Josue Gabriel Navarro Solís
'''
from blockchain import Blockchain
from auxiliarFunctions import *

SHIPMENTS_QTY = 2

if __name__ == "__main__":
    
    #We create the future cheese creator
    cheeseCreator = generateProviders(1)
    
    #We create the cheese that we are going to track
    gourmetCheese = {'Cheese' : 'Camembert'}
    
    #Start Shipment Trace
    shipmentsTrace = Blockchain()
    
    #Now we create the first block (root)
    shipmentsTrace.createBlock(proof=0,originalShipment='0',cheeseAmount=0,product=gourmetCheese,buyer=cheeseCreator.__str__())
    
    #Here we are going to simulate the shipments process
    
    providersGenerated = generateProviders(SHIPMENTS_QTY)
    
    for counting in range(0,SHIPMENTS_QTY):
        
        #Here we create new blocks
        previousBlock = shipmentsTrace.getPreviousBlock()
        previousProof = previousBlock['proof']
        proof = shipmentsTrace.proofOfWork(previousProof)
        previousHash = shipmentsTrace.hash(previousBlock)
        
        #New block info
        cheeseAmount = random.randint(1,1001)
        buyer = providersGenerated[counting]
        newBlock = shipmentsTrace.createBlock(proof,previousHash,cheeseAmount,gourmetCheese,buyer)
    
    shipmentsTrace.__str__()
    
    shipmentsTrace.isChainValid(shipmentsTrace.chain)
    
    
    