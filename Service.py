'''
Created on 13 mar. 2020

@author: bogne
'''
from domain.Eveniment import Eveniment
from domain.Persoana import Persoana
from repository.RepoError import RepoError
import random

class ServiceOrganizareEvenimente(object):
    
    
    def __init__(self, __repoPers, __repoEvent, __valideazaPers, __valideazaEvent):
        self.__repoPers = __repoPers
        self.__repoEvent = __repoEvent
        self.__valideazaPers = __valideazaPers
        self.__valideazaEvent = __valideazaEvent
    
    def __generareId(self):
        id = ''
        for x in range(13):
            id += str(random.randint(0,9))
            
        return id
    
    
    def generarePersoane(self):
        lista_nume = ["Andrei","Andra","Sorin","Ovidiu","Razvan","Andreea","Cosmin","Nicolas","Ioan","Dumitru","Bogdan","Dan","Daniel"]
        lista_adresa = ["Botosani","Cluj","Timisoara","Bucuresti","Targu Mures","Oradea","Arad"]
        for x in range(10):
            id = self.__generareId()
            nume = lista_nume[random.randint(0,len(lista_nume)-1)]
            adresa = lista_adresa[random.randint(0,len(lista_adresa)-1)]
            persoana = Persoana(id,nume,adresa)
            self.__repoPers.adaugaElement(persoana)
    def printPersoane(self):
        if len(self.__repoPers) == 0:
            raise RepoError("lista este goala!\n")
        for pers in self.__repoPers:
            print(pers)    
    def printEvenimente(self):
        if len(self.__repoEvent) == 0:
            raise RepoError("lista este goala!\n") 
        for ev in self.__repoEvent:
            print(ev)       
    def addPerson(self):
        self.__id = input("Introduceti id-ul(cnp-ul) persoanei:\n>>>")
        self.__nume = input("Introduceti numele persoanei:\n>>>")
        self.__adresa = input("Introduceti adresa persoanei:\n>>>")
        
        self.__persoana = Persoana(self.__id, self.__nume, self.__adresa)
        self.__valideazaPers.valideazaPersoana(self.__persoana)
        
        self.__repoPers.adaugaElement(self.__persoana)
        
    
    def addEvent(self):
        self.__id = int(input("Introduceti id-ul evenimentului:\n>>>"))
        self.__data = input("Introduceti data evenimentului:\n>>>")
        self.__timp = input("Introduceti ora evenimentului:\n>>>")
        self.__descriere = input("Introduceti descrierea evenimentului(minim 3 caractere):\n>>>")
        
        self.__eveniment = Eveniment(self.__id, self.__data, self.__timp, self.__descriere)
        self.__valideazaEvent.valideazaEveniment(self.__eveniment)
        
        self.__repoEvent.adaugaElement(self.__eveniment)
        
        
    def updatePerson(self):
        self.__id = input("Introduceti id-ul(cnp-ul) persoanei:\n>>>")
        self.__nume = input("Introduceti numele persoanei:\n>>>")
        self.__adresa = input("Introduceti adresa persoanei:\n>>>")
        
        self.__persoana = Persoana(self.__id, self.__nume, self.__adresa)
        self.__valideazaPers.valideazaPersoana(self.__persoana)
        
        self.__repoPers.modificaElement(self.__persoana)
        
        
    def updateEvent(self):
        self.__id = int(input("Introduceti id-ul evenimentului:\n>>>"))
        self.__data = input("Introduceti data evenimentului:\n>>>")
        self.__timp = input("Introduceti ora evenimentului:\n>>>")
        self.__descriere = input("Introduceti descrierea evenimentului(minim 3 caractere):\n>>>")
        
        self.__eveniment = Eveniment(self.__id, self.__data, self.__timp, self.__descriere)
        self.__valideazaEvent.valideazaEveniment(self.__eveniment)
        
        self.__repoEvent.modificaElement(self.__eveniment)
        
    
    def deletePerson(self):
        self.__id = input("Introduceti id-ul(cnp-ul) persoanei:\n>>>")
        
        
        self.__persoana = Persoana(self.__id, None,None)
        #self.__valideazaPers.valideazaPersoana(self.__persoana)
        
        self.__repoPers.stergereElement(self.__persoana)
        
    def deleteEvent(self):
        self.__id = int(input("Introduceti id-ul evenimentului:\n>>>"))
        
        
        self.__eveniment = Eveniment(self.__id, None,None,None)
        self.__valideazaEvent.valideazaEveniment(self.__eveniment)
        
        self.__repoEvent.stergereElement(self.__eveniment)
        
    def searchPerson(self):
        self.__id = input("Introduceti id-ul(cnp-ul) persoanei:\n>>>")
        self.__persoana = Persoana(self.__id, None, None)
        
        __p1 = self.__repoPers.cautarePersoana(self.__persoana)
        print(__p1)
    
    def searchEvent(self):
        self.__id = int(input("Introduceti id-ul evenimentului:\n>>>"))
        self.__eveniment = Eveniment(self.__id, None,None,None)
        
        __ev = self.__repoEvent.cautareEveniment(self.__eveniment)
        print(__ev)

