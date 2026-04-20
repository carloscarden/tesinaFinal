
from typing import List

from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd



class ProcesadoEnVerbo:
    ''' Aca se guarda todo lo que se puede procesar en un verbo'''
    i = 12345


    def __init__(self, lelsDeMedida: List[LelMmd], lelsCategoricosDeVerbo: List[LelMmd]):

        self.lelsDeMedida=lelsDeMedida 
        ''' 
          lelsDeMedida be the set of objects and subjects in notion of verb that denote 
                numerical attributes
        '''


        self.lelsCategoricosDeVerbo=  lelsCategoricosDeVerbo
        ''' 
          lelsCategoricosDeVerbo be the set of objects and subjects in notion of verb that denote
                categorical attributes
        '''

    def nuevoLelDeMedida(self, unLelDeMedida):
        self.lelsDeMedida.append(unLelDeMedida)

    def nuevoLelCategoricoDeVerbo(self, unLelCategoricoDeVerbo: LelMmd):
        self.lelsCategoricosDeVerbo.append(unLelCategoricoDeVerbo)

    def devolverLelsDeMedida(self):
        if(self.lelsDeMedida):
            return self.lelsDeMedida[0].simbolo
        return ''