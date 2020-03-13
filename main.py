'''
Created on 13 mar. 2020

@author: bogne
'''
from repository.Repository import Repository
from validare.Valideaza import ValideazaEveniment,ValideazaPersoana
from service.Service import ServiceOrganizareEvenimente
from consola.Console import Console


repoPers = Repository()
repoEvent = Repository()
valideazaPers = ValideazaPersoana()
valideazaEvent = ValideazaEveniment()
service = ServiceOrganizareEvenimente(repoPers,repoEvent,valideazaPers,valideazaEvent)
ui = Console(service)
ui.run()