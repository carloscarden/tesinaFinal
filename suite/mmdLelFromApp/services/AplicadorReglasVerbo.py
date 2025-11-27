from typing import List

from suite.mmdLelFromApp.models.diagrama.Diagrama import Diagrama
from suite.mmdLelFromApp.models.diagrama.DiagramasEnVerbo import DiagramasEnVerbo
from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd
from suite.mmdLelFromApp.models.lelsProcesados.ProcesadoEnVerbo import ProcesadoEnVerbo
from suite.mmdLelFromApp.services.ReglasEnVerbo import ReglasEnVerbo



class AplicadorDeReglasVerbo():
    
    def __init__(self, diagrama: Diagrama):
        self.diagramasEnVerbo =DiagramasEnVerbo(diagrama) 
        self.reglasVerbo = ReglasEnVerbo()

    def aplicarReglasDeVerbo(self, lels: List[LelMmd]):

                # REGLA 1
        # Verbs give origin to facts. 
        verbos = self.reglasVerbo.recuperarLosVerbos(lels)
        procesadoEnVerbo = ProcesadoEnVerbo([],[])

        
        for v in verbos:

            # v should be defined as a fact
            hecho = self.diagramasEnVerbo.nuevoHecho(v)
            v.actualizarPosicionDiagramaVerbo(self.diagramasEnVerbo.esquinasVerbo(),
                                              self.diagramasEnVerbo.posicionVerbo)

            # apply Rule 2 to v, get set Mf of measures, add them to f
            # apply Rule 3 to v, get set Df of dimensions, add them to f
            procesadoEnVerbo = self.reglasVerbo.procesarElVerbo( lels, v)

            self.diagramasEnVerbo.generarObjetosDelDiagramaPorVerbo(procesadoEnVerbo, v, hecho)
            
            v.terminadoDeProcesarVerbo()
            self.diagramasEnVerbo.actualizarPosicionVerbo()

        return procesadoEnVerbo.lelsCategoricosDeVerbo
    