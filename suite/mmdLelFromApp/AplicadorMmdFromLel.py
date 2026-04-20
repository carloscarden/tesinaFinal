from django.shortcuts import redirect, render

import json
from suite.mmdLelFromApp.models.diagrama.Diagrama import Diagrama
from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd
from suite.mmdLelFromApp.services.AplicadorReglasSujeto import AplicadorDeReglasSujeto
from suite.mmdLelFromApp.services.AplicadorReglasVerbo import AplicadorDeReglasVerbo
from suite.models import *

class AplicadorMmdFromLel:

    def __init__(self) -> None:
        pass

    def encontrarLosLel(self,sel):
        texto=[]
        for i in sel:
            art=Artefacto.objects.get(id=i)
            if art.tipoDeArtefacto.tipo=="Lel":
                lel = LelMmd()
                lel.initFromDictionary(json.loads(art.texto))
                texto.append(lel)
        
        #texto tendría que devolver los lels de mmdLelFromApp míos, listos para poder analizarlos 
        return texto


    def aplicarMmdFromLel(self, request,idP):
        ok=False
        sel=request.session["lelsSeleccionados"]
        lelsAprocesar = self.encontrarLosLel(sel)
        diagrama = Diagrama([], [])

#        dictDiagrama = diagrama.mock_dict()
 

        aplicadorDeReglasVerbo = AplicadorDeReglasVerbo(diagrama) 
        lelsCategoricosDeVerbo = aplicadorDeReglasVerbo.aplicarReglasDeVerbo(lelsAprocesar)

        aplicadorDeReglasSujeto = AplicadorDeReglasSujeto(diagrama)
        aplicadorDeReglasSujeto.aplicarReglasDeSujeto(lelsCategoricosDeVerbo, lelsAprocesar)

        return render(request,'mmdFromLel.html',{"ok":ok,"diagrama":diagrama.to_dict()})