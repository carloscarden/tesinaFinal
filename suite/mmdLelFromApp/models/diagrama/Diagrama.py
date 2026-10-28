from typing import List
from suite.mmdLelFromApp.models.diagrama.LinkDiagrama import LinkDiagrama

from suite.mmdLelFromApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd




class Diagrama:
    """Clase que mantiene los objetos y los links del diagrama,
       Es la clase que se va a mandar al frontend para que consuma
    """

    def __init__(self, objetosDelDiagrama: List[ObjetoDiagrama] , linksDelDiagrama: List[LinkDiagrama]):
        self._objetosDelDiagrama= objetosDelDiagrama
        self._linksDelDiagrama= linksDelDiagrama


    @property
    def objetos(self) -> List[ObjetoDiagrama]:
        return self._objetosDelDiagrama

    @property
    def links(self) -> List[LinkDiagrama]:
        return self._linksDelDiagrama


    def agregar_objeto(self, objeto: ObjetoDiagrama) -> ObjetoDiagrama:
        self._objetosDelDiagrama.append(objeto)
        return objeto
    
    def agregar_link(self, link: LinkDiagrama) -> LinkDiagrama:
        self._linksDelDiagrama.append(link)
        return link

    def generarLinks(self,desdeExpresion, lelsCategoricos: List[LelMmd]):
        for lel in lelsCategoricos:
            nuevoLink = LinkDiagrama(desdeExpresion, lel.simbolo)
            self._linksDelDiagrama.append(nuevoLink)

    def to_dict(self):
            return {
                'objetosDelDiagrama': [objeto.to_dict() for objeto in self._objetosDelDiagrama],
                'linksDelDiagrama': [link.to_dict() for link in self._linksDelDiagrama]
            }

