'''
Instituto Tecnológico de Costa Rica
Escuela de Ingeniería en Computación
Criptografía
Autores:
Luis Carlos Araya Mata
Rolbin Méndez Brenes
Josue Gabriel Navarro Solís
'''
from provider import Provider
import random, pickle

def generateProviders(amount : int) -> list:
    '''
    '''
    #CHEESE_NAMES = ["Beaufort d' Ete",'Rogue River Blue', 'Gorau Glas', 'Winnimere', 'Cacio Bufala', 'Caciocavallo']
    providers : list = []        
    PROVIDERS_NAMES : list = ['iGourmet','Harry & David','Murrays Cheese', 'Hickory Farms', 'Caputo Market', 'Zingermans']
    COUNTRIES : list = ['Germany', 'Switzerland', 'France', 'Denmark', 'Russia', 'Luxembourg']
    RELEVANCE : list = ['Transnational','National','Local']
    
    for count in range(0,amount):
        newName = PROVIDERS_NAMES[random.randint(0,len(PROVIDERS_NAMES) - 1)]
        newCountry = COUNTRIES[random.randint(0, len(COUNTRIES) - 1)]
        newRelevance = RELEVANCE[random.randint(0,len(RELEVANCE) - 1)]
        newProvider = Provider(newName , newCountry , newRelevance)
        providers.append(newProvider)
    
    return providers[0] if len(providers) == 1 else providers

def saveBlockChain(chain : list) -> None:
    '''
    '''
    with open('blockchain.pkl','wb') as newChain:
        pickle.dump(chain,newChain)
    
def loadChain() -> list:
    '''
    '''
    with open('blockchain.pkl','rb') as savedChain:
        return pickle.load(savedChain)
    
def simulateShipments():
    '''
    '''