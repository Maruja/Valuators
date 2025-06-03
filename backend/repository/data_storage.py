'''This absract class is meant to work as an java interface where 
it will have the definition of the methods and each subclass will maanage to 
implemen in their own necesarry style, reading_from_file or reading_from_db '''
from abc import ABC, abstractmethod

#defining the interface 
class DataStorage():
    
    @abstractmethod
    def load(self):
        """loading data from storage eeiher cvs or db for now"""
        pass

    @abstractmethod
    def save(self, address):
        """saving an insertion in cvvs or db"""
        pass

