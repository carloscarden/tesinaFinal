from typing import List

from suite.mmdLelFromApp.builders.DiagramaBuilder import DiagramaBuilder
from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd
from suite.mmdLelFromApp.models.lelsProcesados.ProcesadoEnSujeto import ProcesadoEnSujeto



class DiagramasEnSujeto:
    """Clase para construir los diagramas que apareceran en los sujetos
    """
    i = 12345

    def __init__(self, builder: DiagramaBuilder):
        self.diagramaBuilder = builder


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
            self.diagramaBuilder.crear_link_hecho(sujeto.simbolo, nivel.simbolo)


    def nuevosArcosMultiples(self, lelsArcosMultiples: List[LelMmd], sujeto: LelMmd):
        for lelMultiple in lelsArcosMultiples:
            self.diagramaBuilder.crear_link_multiple(sujeto.simbolo, lelMultiple.simbolo)
            self.nuevoNodoMultiple(sujeto, lelMultiple)

    def nuevosArcosOpcionales(self, lelsArcosOpcionales: List[LelMmd],sujeto: LelMmd):
        for lelOpcional in lelsArcosOpcionales:
            self.diagramaBuilder.crear_link_opcional(sujeto.simbolo, lelOpcional.simbolo)
            self.nuevoNodoOpcional(sujeto, lelOpcional)

    def nuevosNivelesNoProcesados(self, lelsDeNivelNoProcesados: List[LelMmd],sujeto: LelMmd):
        for lelNoProcesados in lelsDeNivelNoProcesados:
            self.nuevoNodoNoProcesado(sujeto, lelNoProcesados)

    def nuevasPropiedades(self,  lelsDePropiedad: List[LelMmd], sujeto: LelMmd):
        for lelPropiedad in lelsDePropiedad:
            self.diagramaBuilder.crear_link_hecho(sujeto.simbolo, lelPropiedad.simbolo)
            self.nuevaPropiedad(sujeto, lelPropiedad)
            

    def nuevoNodoMultiple(self, sujeto: LelMmd, lelMultiple: LelMmd):
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelMultiple.actualizarPosicionDiagramaSujeto(sujeto.getCalculadorSujeto(), posicionNueva)
            
        self.diagramaBuilder.crear_nivel(lelMultiple.simbolo, sujeto.simbolo, posicionNueva)


    def nuevoNodoOpcional(self, sujeto: LelMmd, lelOpcional: LelMmd):       
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelOpcional.actualizarPosicionDiagramaSujeto(sujeto.getCalculadorSujeto(), posicionNueva)
            
        self.diagramaBuilder.crear_opcional(lelOpcional.simbolo, sujeto.simbolo, posicionNueva)
        lelOpcional.terminadoDeDibujarNodo()


    def nuevoNodoNoProcesado(self, sujeto: LelMmd, lelNoProcesado: LelMmd):
        if(lelNoProcesado.estaDibujado()):
            return
        
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelNoProcesado.actualizarPosicionDiagramaSujeto(sujeto.getCalculadorSujeto(), posicionNueva)
        
        self.diagramaBuilder.crear_nivel(lelNoProcesado.simbolo, sujeto.simbolo, posicionNueva)
        lelNoProcesado.terminadoDeDibujarNodo()

        
    def nuevaPropiedad(self, sujeto: LelMmd, lelPropiedad: LelMmd):
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelPropiedad.actualizarPosicionDiagrama(posicionNueva)
        self.diagramaBuilder.crear_propiedad(lelPropiedad.simbolo, sujeto.simbolo, posicionNueva)
        lelPropiedad.terminadoDeDibujarNodo()
            
