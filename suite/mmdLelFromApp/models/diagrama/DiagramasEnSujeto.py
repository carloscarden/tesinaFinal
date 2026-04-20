from typing import List

from suite.mmdLelFromApp.models.diagrama import Diagrama
from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd
from suite.mmdLelFromApp.models.lelsProcesados.ProcesadoEnSujeto import ProcesadoEnSujeto



class DiagramasEnSujeto:
    """Clase para construir los diagramas que apareceran en los sujetos
    """
    i = 12345

    def __init__(self, unDiagrama: Diagrama):
        self.diagrama = unDiagrama


    def generarObjetosDelDiagramaPorSujeto(self, procesadoEnSujeto: ProcesadoEnSujeto, sujeto: LelMmd):
        # all the elements in lelsDeMedida should be defined as 
        # measures of the fact corresponding to v
        self.nuevosNivelesProcesados(procesadoEnSujeto.lelsDeNivel, sujeto)
        self.nuevosArcosMultiples(procesadoEnSujeto.lelsArcosMultiples, sujeto)
        self.nuevosArcosOpcionales(procesadoEnSujeto.lelsArcosOpcionales, sujeto)
        self.nuevosNivelesNoProcesados(procesadoEnSujeto.lelsDeNivelNoProcesados, sujeto)
        self.nuevasPropiedades(procesadoEnSujeto.lelsDePropiedad, sujeto)


    def nuevosNivelesProcesados(self,  lelsDeNivel: List[LelMmd], sujeto: LelMmd):
        for nivel in lelsDeNivel:
            self.diagrama.nuevoLinkHecho(sujeto.simbolo, nivel.simbolo)


    def nuevosArcosMultiples(self, lelsArcosMultiples: List[LelMmd], sujeto: LelMmd):
        for lelMultiple in lelsArcosMultiples:
            self.diagrama.nuevoLinkMultiple(sujeto.simbolo, lelMultiple.simbolo)
            self.nuevoNodoMultiple(sujeto, lelMultiple)

    def nuevosArcosOpcionales(self, lelsArcosOpcionales: List[LelMmd],sujeto: LelMmd):
        for lelOpcional in lelsArcosOpcionales:
            self.diagrama.nuevoLinkOpcional(sujeto.simbolo, lelOpcional.simbolo)
            self.nuevoNodoOpcional(sujeto, lelOpcional)

    def nuevosNivelesNoProcesados(self, lelsDeNivelNoProcesados: List[LelMmd],sujeto: LelMmd):
        for lelNoProcesados in lelsDeNivelNoProcesados:
            self.nuevoNodoNoProcesado(sujeto, lelNoProcesados)

    def nuevasPropiedades(self,  lelsDePropiedad: List[LelMmd], sujeto: LelMmd):
        for lelPropiedad in lelsDePropiedad:
            self.diagrama.nuevoLinkHecho(sujeto.simbolo, lelPropiedad.simbolo)
            self.nuevaPropiedad(sujeto, lelPropiedad)
            

    def nuevoNodoMultiple(self, sujeto: LelMmd, lelMultiple: LelMmd):
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelMultiple.actualizarPosicionDiagramaSujeto(sujeto.getCalculadorSujeto(), posicionNueva)
            
        self.diagrama.nuevoObjetoNivelDelDiagrama(lelMultiple.simbolo, sujeto.simbolo, posicionNueva)


    def nuevoNodoOpcional(self, sujeto: LelMmd, lelOpcional: LelMmd):       
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelOpcional.actualizarPosicionDiagramaSujeto(sujeto.getCalculadorSujeto(), posicionNueva)
            
        self.diagrama.nuevoObjetoOpcionalDelDiagrama(lelOpcional.simbolo, sujeto.simbolo, posicionNueva)
        lelOpcional.terminadoDeDibujarNodo()


    def nuevoNodoNoProcesado(self, sujeto: LelMmd, lelNoProcesado: LelMmd):
        if(lelNoProcesado.estaDibujado()):
            return
        
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelNoProcesado.actualizarPosicionDiagramaSujeto(sujeto.getCalculadorSujeto(), posicionNueva)
        
        self.diagrama.nuevoObjetoNivelDelDiagrama(lelNoProcesado.simbolo, sujeto.simbolo, posicionNueva)
        lelNoProcesado.terminadoDeDibujarNodo()

        
    def nuevaPropiedad(self, sujeto: LelMmd, lelPropiedad: LelMmd):
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelPropiedad.actualizarPosicionDiagrama(posicionNueva)
        self.diagrama.nuevoObjetoPropiedadDelDiagrama(lelPropiedad.simbolo, sujeto.simbolo, posicionNueva)
        lelPropiedad.terminadoDeDibujarNodo()
            
