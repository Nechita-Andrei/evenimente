'''
Created on 13 mar. 2020

@author: bogne
'''
from repository.RepoError import RepoError
from validare.ValidError import ValidError


class Console(object):
     
    def __init__(self, __service):
        self.__service = __service
        self.__actiunePersoane ={
                                "addPerson"    : self.__service.addPerson,
                                "deletePerson" : self.__service.deletePerson,
                                "modifyPerson" : self.__service.updatePerson,
                                "searchPerson" : self.__service.searchPerson,
                                "printPerson"  : self.__service.printPersoane
                                }
        self.__actiuneEvenimente ={
                                "addEvent"    : self.__service.addEvent,
                                "deleteEvent" : self.__service.deleteEvent,
                                "modifyEvent" : self.__service.updateEvent,
                                "searchEvent" : self.__service.searchEvent,
                                "printEvent"  : self.__service.printEvenimente
                                }
    
    
    
    def __ui(self):
        print("ADAUGARE")
        print("addPerson. Adauga o persoana noua in lista.")
        print("addEvent. Adauga un eveniment nou in lista.")
        print("\nSTERGERE")
        print("deletePerson. Sterge o persoana din lista.")
        print("deleteEvent. Sterge un eveniment din lista.")
        print("\nMODIFICARE")
        print("modifyPerson. Modifica o persoana din lista.")
        print("modifyEvent. Modifica un eveniment din lista")
        print("\nCAUTARE")
        print("searchPerson. Cauta persoana dupa nume si adresa")
        print("searchEvent. Cauta un eveniment dupa data si ora")
        
        ###TO DO: Iteratia 2
        print("\nComenzi ajutatoare")
        print("printPerson. Printeaza toate persoanele")
        print("printEvent. Printeaza toate evenimentele")
        print("exit. Iesire din aplicatie")
    
    
    def run(self):
        self.__ui()
        self.__service.generarePersoane()
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                return
            else:
                try:
                    if cmd in self.__actiunePersoane:
                        self.__actiunePersoane[cmd]()
                    elif cmd in self.__actiuneEvenimente:
                        self.__actiuneEvenimente[cmd]()
                    else: print("comanda invalida!\n")
                except ValueError as msg:
                    print(msg)
                except ValidError as msg:
                    print(msg)   
                except RepoError as msg:
                    print(msg)
            
                


