from suite.mmdLelFromApp.models.diagrama.Diagrama import Diagrama
from suite.mmdLelFromApp.models.diagrama.LinkDiagrama import LinkDiagrama
from suite.mmdLelFromApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama


class DiagramaBuilder:
    def __init__(self, diagrama: Diagrama):
        self.diagrama = diagrama

    def crear_hecho(self, simbolo, posicion):
        hecho = ObjetoDiagrama.nuevoHecho(
            simbolo,
            posicion
        )
        self.diagrama.agregar_objeto(hecho)
        return hecho
    
    def crear_dimension(self, simbolo, verboSimbolo, posicion):
        dimension = ObjetoDiagrama.nuevaDimension(
            simbolo,
            verboSimbolo,
            posicion
        )
        self.diagrama.agregar_objeto(dimension)
        return dimension
    
    def crear_nivel(self, simbolo, sujetoSimbolo, posicion):
        nivel = ObjetoDiagrama.nuevoNivel(
            simbolo,
            sujetoSimbolo,
            posicion
        )
        self.diagrama.agregar_objeto(nivel)
        return nivel
    
    def crear_propiedad(self, simbolo, sujetoSimbolo, posicion):
        propiedad = ObjetoDiagrama.nuevaPropiedad(
            simbolo,
            sujetoSimbolo,
            posicion
        )
        self.diagrama.agregar_objeto(propiedad)
        return propiedad
    
    def crear_opcional(self, simbolo, sujetoSimbolo, posicion):
        opcional = ObjetoDiagrama.nuevoLelOpcional(
            simbolo,
            sujetoSimbolo,
            posicion
        )
        self.diagrama.agregar_objeto(opcional)
        return opcional
    
    def crear_link_hecho(self, sujetoSimbolo, nivelSimbolo):
        link = LinkDiagrama.nuevoHecho(
            sujetoSimbolo,
            nivelSimbolo
        )
        self.diagrama.agregar_link(link)
        return link
    

    def crear_link_multiple(self, sujetoSimbolo, lelMultipleSimbolo):
        link = LinkDiagrama.nuevoLinkMultiple(
            sujetoSimbolo,
            lelMultipleSimbolo
        )
        self.diagrama.agregar_link(link)
        return link

    def crear_link_opcional(self, sujetoSimbolo, lelOpcionalSimbolo):
        link = LinkDiagrama.nuevoLinkOpcional(
            sujetoSimbolo,
            lelOpcionalSimbolo
        )
        self.diagrama.agregar_link(link)
        return link

    def crear_link_dimension(self, lelDimensionSimbolo, verboLelSimbolo):
        link = LinkDiagrama.nuevoLinkDimension(
            verboLelSimbolo,
            lelDimensionSimbolo
        )
        self.diagrama.agregar_link(link)
        return link 
    
    def crear_link_del_diagrama(self, linkDelDiagrama):
        self.diagrama.agregar_link(linkDelDiagrama)
        return linkDelDiagrama