'''
Created on 13 mar. 2020

@author: bogne
'''
from validare.ValidError import ValidError

class ValideazaPersoana(object):
        
    
    def valideazaPersoana(self,persoana):
        erori = ""
        if not len(persoana.get_id()) == 13:
            erori += "id invalid!\n"
        if persoana.get_nume() == "":
            erori += "nume invalid!\n"
        if len(persoana.get_adresa()) <= 3:
            erori += "adresa invalida!\n"
        
        if len(erori) != 0:
            raise ValidError(erori)

    


class ValideazaEveniment(object):
    
    def valideazaEveniment(self,event):
        erori = ""
        if event.get_id() < 1:
            erori += "id invalid!\n"
        ok = False
        data = event.get_data().split("/")
        if len(data) == 3:
            if int(data[0]) > 0 and int(data[0]) < 32:
                if int(data[1]) > 0 and int(data[1]) < 13:
                    if int(data[2]) > 2017 and int(data[2]) < 2020:
                        ok = True
        
        if ok == False:
            erori += "data invalida!\n"
        
        ora = event.get_timp().split(":")
        if int(ora[0])<0 or int(ora[0])> 23 or int(ora[1])<0 or int(ora[1])>59:
            erori += "ora invalida!\n"
        
        if len(event.get_descriere()) <3:
            erori += "descriere invalida!\n"
            
        if erori != "":
            raise ValidError(erori)
            
            


