

from suite.mmdLelFromApp.models.diagrama.ConstantesPosiciones import ConstantesPosiciones
from suite.mmdLelFromApp.models.diagrama.LadosDiagramaVerbo import LadosDiagramaVerbo
from suite.mmdLelFromApp.models.lel.CalculadorPosicionSujeto import CalculadorPosicionSujeto


class CalculadorPosicionVerbo:

    i = 12345

    def __init__(self,  unasEsquinas = None, anguloNodo =None):
        self.esquinasVerbo = unasEsquinas
        self.ladoAusar = 0
        self.corrimientoPosiciones = [0,0,0,0]
        self.anguloNodo = anguloNodo
        self.mapeoDeLadosYangulos = { 
            LadosDiagramaVerbo.LADO_SUPERIOR.value: ConstantesPosiciones.ANGULO_APERTURA_LADO_ARRIBA.value,
            LadosDiagramaVerbo.LADO_INFERIOR.value: ConstantesPosiciones.ANGULO_APERTURA_LADO_DERECHO.value,
            LadosDiagramaVerbo.LADO_IZQUIERDO.value: ConstantesPosiciones.ANGULO_APERTURA_LADO_ABAJO.value,
            LadosDiagramaVerbo.LADO_DERECHO.value: ConstantesPosiciones.ANGULO_APERTURA_LADO_IZQUIERDO.value 
        }


    def nuevaEsquinaVerbo(self, esquinasVerbo):
        self.esquinasVerbo = esquinasVerbo


    def calcularPosicionProximoNodo(self):
        self.anguloNodo = self.mapeoDeLadosYangulos[self.ladoAusar]
        posicionX = self.esquinasVerbo[self.ladoAusar][0] + self.corrimientoPosiciones[self.ladoAusar]
        posicionY = self.esquinasVerbo[self.ladoAusar][1]
        return (posicionX, posicionY) 


    def actualizarPosiciones(self):
        self.actualizarCorrimientosDeLosNodos()
        self.actualizarLadoAusar()


    def actualizarCorrimientosDeLosNodos(self):
        self.corrimientoPosiciones[self.ladoAusar] = self.corrimientoPosiciones[self.ladoAusar] + ConstantesPosiciones.CORRIMIENTO_POSICION.value


    def actualizarLadoAusar(self):
        self.ladoAusar += 1
        if(self.ladoAusar == 4):
            self.ladoAusar = 0

    def getCalculadorPosicionSujeto(self):
        return CalculadorPosicionSujeto(self.anguloNodo)

    def __str__(self):
        return f"CalculadorVerbo(esquinas={self.esquinasVerbo}, ladoAusar={self.ladoAusar}, posiciones={self.corrimientoPosiciones} "
    

    def __repr__(self) -> str:
        return f"CalculadorVerbo(esquinas={self.esquinasVerbo}, ladoAusar={self.ladoAusar}, posiciones={self.corrimientoPosiciones} "