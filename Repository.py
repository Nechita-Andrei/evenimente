'''
Created on 13 mar. 2020

@author: bogne
'''
from repository.RepoError import RepoError
class Repository():
    
    
    def __init__(self):
        self.__elem = []
    
    
    
    def __len__(self):
        return len(self.__elem)
    
    def __getitem__(self,value):
        return self.__elem[value]
    
    def adaugaElement(self,elem):
        '''
        Adauga un element in lista cu elemente
        in: elem
        pre: elem - obiectul pe care vrem sa-l stocam
        raise RepoError daca obiectul deja exista
        '''
        for x in self.__elem:
            if x == elem: raise RepoError("obiectul exista deja!\n")
        
        self.__elem.append(elem)
    
    def modificaElement(self,elem):
        '''
        Modifica un element deja existent cu unul nou
        in: elem
        pre: elem--obiectul pe care vrem sa-l stocam
        raise RepoError daca obiectul nu exista
        '''
        for i in range(len(self.__elem)):
            if self.__elem[i] == elem:
                self.__elem[i] = elem
                return
        
        raise RepoError("elementul nu a putut fi identificat\n!")
    def stergereElement(self,elem):
        '''
        Sterge elementul 'elem' din lista
        in: elem
        pre: elem - obiectul pe care il stergem
        '''
        for el in self.__elem:
            if el == elem:
                self.__elem.remove(el)
                return
        
        raise RepoError("obiectul nu exista!\n")
    
    def cautarePersoana(self,persoana):
        '''
        Cauta persoana in functie de id sau nume si adresa
        in: persoana
        pre: persoana - obiectul de tipul persoana ce trebuie sa contina numele si adresa
        post : Persoana cautata
        raise RepoError daca persoana nu este gasita
        '''
        for pers in self.__elem:
            if pers == persoana:
                return pers
        
        raise RepoError("persoana nu exista!\n")
    
    def cautareEveniment(self,event):
        '''
        Cauta evenimentul in functie de id sau data si ora si descrierea
        in: event
        pre: event- evenimentul de tipul eveniment ce trebuie sa contina data si ora
        post: Evenimentul cautat
        raise RepoError daca evenimentul nu este gasit
        '''
        for ev in self.__elem:
            if event == ev:
                return ev
        raise RepoError("evenimentul nu exista!\n")
    
    