from typing import List

from suite.mmdLelFromApp.models.diagrama.Diagrama import Diagrama
from suite.mmdLelFromApp.models.diagrama.DiagramasEnSujeto import DiagramasEnSujeto
from suite.mmdLelFromApp.models.diagrama.LinkDiagrama import LinkDiagrama
from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd
from suite.mmdLelFromApp.services.ReglasEnSujeto import ReglasEnSujeto



class AplicadorDeReglasSujeto():


    def __init__(self, unDiagrama: Diagrama) -> None:
        self.diagramasEnSujeto = DiagramasEnSujeto(unDiagrama)
        self.reglas = ReglasEnSujeto()

    def aplicarReglasDeSujeto(self, lelsCategoricosDeVerbo: List[LelMmd], lels: List[LelMmd]):

        lelsAprocesar = lelsCategoricosDeVerbo


        while 1:
            hayMasLels = []

            for sujeto in  lelsAprocesar:

                # Encontrar todos los Categorical objects and subjects del sujeto
                encontradoEnSujeto  = self.reglas.encontrarLosObjetosCategoricosDeSujetos(sujeto)

                #apply Rule 4 to o, get set Cl of levels, add them to l as children levels
                #apply Rule 5 to o, get set Pl of properties, add them to l as children levels
                #apply Rule 6 to o and o′, possibly change the arc from l to l′to multiple
                #apply Rule 7 to o and o′, possibly change the arc from l to l′to optional
                procesadoEnSujeto = self.reglas.procesarElSujeto(encontradoEnSujeto, lels)
                self.diagramasEnSujeto.generarObjetosDelDiagramaPorSujeto(procesadoEnSujeto, sujeto)

                
                hayMasLels.extend(procesadoEnSujeto.lelsDeNivelNoProcesados)
                sujeto.terminadoDeProcesar()

            if not hayMasLels:
                break
            else:
                lelsAprocesar = hayMasLels

