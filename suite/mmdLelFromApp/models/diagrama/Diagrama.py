from typing import List
from suite.mmdLelFromApp.models.diagrama.LinkDiagrama import LinkDiagrama

from suite.mmdLelFromApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd




class Diagrama:
    """Clase que mantiene los objetos y los links del diagrama,
       Es la clase que se va a mandar al frontend para que consuma
    """
    i = 12345

    def __init__(self, objetosDelDiagrama , linksDelDiagrama):
        self.objetosDelDiagrama= objetosDelDiagrama
        self.linksDelDiagrama= linksDelDiagrama
    
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


    def mock_dict(self):

        o1= ObjetoDiagrama("ADMINISTER",  "Doseaaa",  "Class" , "800", "50")
        o2= ObjetoDiagrama("date",  "Property" ,"970","150" )
        o3= ObjetoDiagrama("patient", "Property" ,"650","-50"  )
        o4= ObjetoDiagrama("seriousness", "Property" ,"650","40"  )
        o5= ObjetoDiagrama("disease", "Doseaaa" ,"650","150" )
        o6= ObjetoDiagrama("hour",  "Property" ,"800","150"  )
        o7= ObjetoDiagrama("drug",  "Property" ,"970","-50"  )
        o8= ObjetoDiagrama("outcome",  "Doseaaa" ,"970","40" )
        o9= ObjetoDiagrama("doctor",  "Property", "800", "-50" )

        os = [o1 ,o2 ,o3 ,o4 ,o5 ,o6 ,o7 ,o8 ,o9]

        link1 = LinkDiagrama("ADMINISTER", "patient", "linkNormal")
        link2 = LinkDiagrama("patient", "city", "linkNormal")
        link3 = LinkDiagrama("city", "state", "linkNormal")
        link4 = LinkDiagrama("state", "country", "linkNormal")
        link5 = LinkDiagrama("ADMINISTER", "doctor", "linkOpcional")
        link6 = LinkDiagrama("doctor", "depto", "linkNormal")
        link7 = LinkDiagrama("depto", "doctor", "linkNormal")
        link8 = LinkDiagrama("depto", "hospital", "linkNormal")
        link9 = LinkDiagrama("hospital", "city", "linkNormal")
        link10 = LinkDiagrama("ADMINISTER", "seriousness", "linkNormal")
        link11 = LinkDiagrama("ADMINISTER", "disease", "linkNormal")
        link12 = LinkDiagrama("ADMINISTER", "drug", "linkNormal")

        ls = [link1 ,link2 ,link3 ,link4 ,link5 ,link6 ,link7 ,link8 ,link9 ,link10 ,link11 ,link12]

        self.objetosDelDiagrama = os
        self.linksDelDiagrama = ls

        return self.to_dict()