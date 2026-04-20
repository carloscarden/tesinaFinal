from typing import List
from suite.mmdLelFromApp.models.diagrama.LinkDiagrama import LinkDiagrama

from suite.mmdLelFromApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd




class Diagrama:
    """Clase que mantiene los objetos y los links del diagrama,
       Es la clase que se va a mandar al frontend para que consuma
    """

    def __init__(self, objetosDelDiagrama: List[ObjetoDiagrama] , linksDelDiagrama: List[LinkDiagrama]):
        self.objetosDelDiagrama= objetosDelDiagrama
        self.linksDelDiagrama= linksDelDiagrama

    def agregar_objeto(self, objeto: ObjetoDiagrama) -> ObjetoDiagrama:
        self.objetosDelDiagrama.append(objeto)
        return objeto
    
    def agregar_link(self, link: LinkDiagrama) -> LinkDiagrama:
        self.linksDelDiagrama.append(link)
        return link

    
    def nuevoHechoDelDiagrama(self, lelVerboSimbolo, posicionNueva) -> ObjetoDiagrama:
        nuevoHecho = ObjetoDiagrama.nuevoHecho(lelVerboSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevoHecho)
        return nuevoHecho
    
    def nuevoObjetoDimensionDelDiagrama(self, lelDimensionSimbolo, verboLelSimbolo, posicionNueva):
        nuevaDimension = ObjetoDiagrama.nuevaDimension(lelDimensionSimbolo, verboLelSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevaDimension)

    
    def nuevoObjetoNivelDelDiagrama(self, lelNivelSimbolo, sujetoSimbolo, posicionNueva):
        nuevoNivel = ObjetoDiagrama.nuevoNivel(lelNivelSimbolo, sujetoSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevoNivel)

    def nuevoObjetoPropiedadDelDiagrama(self, lelSimbolo, sujetoSimbolo, posicionNueva):
        nuevaPropiedad = ObjetoDiagrama.nuevaPropiedad(lelSimbolo, sujetoSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevaPropiedad)

    def nuevoObjetoOpcionalDelDiagrama(self, lelSimbolo, sujetoSimbolo, posicionNueva):
        nuevoObjetoOpcional = ObjetoDiagrama.nuevoLelOpcional(lelSimbolo, sujetoSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevoObjetoOpcional)
    

    def nuevoLinkHecho(self, sujetoSimbolo, nivelSimbolo):
        nuevoLink= LinkDiagrama.nuevoHecho( sujetoSimbolo, nivelSimbolo)
        self.linksDelDiagrama.append(nuevoLink)

    def nuevoLinkMultiple(self, sujetoSimbolo, lelMultipleSimbolo):   
        nuevoLink = LinkDiagrama.nuevoLinkMultiple( sujetoSimbolo, lelMultipleSimbolo)
        self.linksDelDiagrama.append(nuevoLink)

    def nuevoLinkOpcional(self, sujetoSimbolo, lelOpcionalSimbolo):
        nuevoLink= LinkDiagrama.nuevoLinkOpcional(sujetoSimbolo, lelOpcionalSimbolo)
        self.linksDelDiagrama.append(nuevoLink)

    def nuevoLinkDimensionDelDiagrama(self, lelDimensionSimbolo, verboLelSimbolo):
        nuevoLink = LinkDiagrama.nuevoLinkDimension(verboLelSimbolo, lelDimensionSimbolo)
        self.linksDelDiagrama.append(nuevoLink)
    
    def nuevoLinkDelDiagrama(self, linkDelDiagrama):
        self.linksDelDiagrama.append(linkDelDiagrama)

    def generarLinks(self,desdeExpresion, lelsCategoricos: List[LelMmd]):
        for lel in lelsCategoricos:
            nuevoLink = LinkDiagrama(desdeExpresion, lel.simbolo)
            self.linksDelDiagrama.append(nuevoLink)

    def to_dict(self):
            return {
                'objetosDelDiagrama': [objeto.to_dict() for objeto in self.objetosDelDiagrama],
                'linksDelDiagrama': [link.to_dict() for link in self.linksDelDiagrama]
            }

