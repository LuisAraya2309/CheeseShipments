'''
Instituto Tecnológico de Costa Rica
Escuela de Ingeniería en Computación
Criptografía
Autores:
Luis Carlos Araya Mata
Rolbin Méndez Brenes
Josue Gabriel Navarro Solís
'''

class Provider:
    
    def __init__(self, newName : str, newCountry : str, newRelevance : str):
        '''
        '''
        self.name = newName
        self.country = newCountry
        self.relevance = newRelevance
        
    def __str__(self):
        '''
        '''
        return f'Name : {self.name} \nCountry : {self.country} \nRelevance : {self.relevance}\n'
        