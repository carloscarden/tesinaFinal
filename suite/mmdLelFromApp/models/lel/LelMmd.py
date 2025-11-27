from spacy.tokens import Doc
from suite.mmdLelFromApp.models.lel.CalculadorPosicionVerbo import CalculadorPosicionVerbo
from suite.mmdLelFromApp.models.lel.DatosParaPosicionDiagrama import DatosParaPosicionDiagrama

from suite.mmdLelFromApp.models.lel.DatosParaProcesoDiagrama import DatosParaProcesoDiagrama



class LelMmd:
    '''El LEL es un glosario
en el cual se definen símbolos (términos o frases), y cada símbolo se define a través
de dos atributos: la noción y los impactos'''
    
    i = 12345

    def __init__(self, categoria: str = None, simbolo: str= None, nocion: str= None):
        self.categoria = categoria

        self.simbolo = simbolo
        '''
        símbolos (términos o frases)
        '''

        self.nocion = nocion
        ''' 
        La noción describe la denotación, es decir, describe las características intrínsecas 
        y sustanciales del símbolo
        '''

        self.datosParaProceso = DatosParaProcesoDiagrama()
        '''
        Datos necesarios para el procesamiento del diagrama'''

        self.datosParaPosicionDiagrama = DatosParaPosicionDiagrama()
        '''
        Datos necesarios para la construccion del nodo '''

    def initFromDictionary(self, lelDict):
        self.simbolo = lelDict["nombre"]
        self.categoria = lelDict["category"]
        self.nocion = lelDict["notion"]


    def devolverDocNotion(self, nlp) -> Doc:
        return self.datosParaProceso.miDocNotion(nlp, self.nocion)
    
    def estaProcesado(self):
        return self.datosParaProceso.procesadoLel
    
    def terminadoDeProcesar(self):
        self.datosParaProceso.procesadoLel = True

    def actualizarPosicionDiagrama(self, posicion):
        self.datosParaPosicionDiagrama.nuevaPosicionDiagrama(posicion)


    def actualizarPosicionDiagramaVerbo(self, esquinasVerbo, posicionVerbo):
        calculadorPosicionVerbo = CalculadorPosicionVerbo(esquinasVerbo)
        self.datosParaPosicionDiagrama.nuevoCalculadorPosicionVerbo(calculadorPosicionVerbo)
        self.datosParaPosicionDiagrama.nuevaPosicionDiagrama(posicionVerbo)


    def actualizarPosicionDiagramaSujeto(self, unCalculadorPosicionSujeto, posicionSujeto):
        self.datosParaPosicionDiagrama.nuevoCalculadorPosicionSujeto(unCalculadorPosicionSujeto)
        self.datosParaPosicionDiagrama.nuevaPosicionDiagrama(posicionSujeto)

        
    def getPosicionParaNodoDeVerbo(self):
        return self.datosParaPosicionDiagrama.calcularPosicionProximoNodoParaVerbo()

    def getPosicionParaNodoDeSujeto(self):
        return self.datosParaPosicionDiagrama.calcularPosicionProximoNodo()
    
    def terminadoDeProcesarVerbo(self):
        self.datosParaProceso.nuevoVerbo()

    def terminadoDeProcesarPropiedad(self):
        self.datosParaProceso.nuevaPropiedad()

    def terminadoDeDibujarNodo(self):
        self.datosParaProceso.terminadoDeDibujarNodo()

    def terminadoDeProcesarMedida(self):
        self.datosParaProceso.nuevaMedidaEnVerbo()

    def getCalculadorPosicionSujeto(self):
        return self.datosParaPosicionDiagrama.getCalculadorPosicionSujeto()


    def getCalculadorSujeto(self):
        return self.datosParaPosicionDiagrama.getCalculadorSujeto()

    def estaDibujado(self):
        self.datosParaProceso.estaDibujado()

    def __str__(self):
        return f"Lel(categoria={self.categoria}, simbolo={self.simbolo}), \ndatosParaPosicion={self.datosParaPosicionDiagrama} "
    

    def __repr__(self) -> str:
        return f"Lel(categoria={self.categoria}, simbolo={self.simbolo}), \ndatosParaPosicion={self.datosParaPosicionDiagrama}, "