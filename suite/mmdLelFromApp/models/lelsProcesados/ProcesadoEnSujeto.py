from typing import List

from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd


class ProcesadoEnSujeto:
    ''' Aca se guarda todo lo que se puede procesar en un sujeto'''
    i = 12345

    def __init__(self, lelsDePropiedad: List[LelMmd], lelsDeNivel: List[LelMmd], lelsDeNivelNoProcesados: List[LelMmd],
                  lelsArcosOpcionales: List[LelMmd], lelsArcosMultiples: List[LelMmd]):
        self.lelsDePropiedad=lelsDePropiedad
        ''' 
        lelsDePropiedad be the set of objects and subjects in subject that denote numerical attributes
        '''

        self.lelsDeNivel=  lelsDeNivel
        ''' 
         lelsDeNivel be the set of objects and subjects in subject that denote categorical attributes
        '''

        self.lelsDeNivelNoProcesados=  lelsDeNivelNoProcesados
        ''' 
         lelsDeNivelNoProcesados son los nuevos lels de nivel a dibujar y también a procesar
        '''

        self.lelsArcosOpcionales = lelsArcosOpcionales
        ''' 
         lelsArcosOpcionales son lels de arco opcional a dibujar y también a procesar
        '''

        self.lelsArcosMultiples = lelsArcosMultiples

    def nuevoLelDePropiedad(self, unLelDePropiedad: LelMmd):
        self.lelsDePropiedad.append(unLelDePropiedad)

    def nuevoLelDeNivel(self, unLelDeNivel: LelMmd):
        self.lelsDeNivel.append(unLelDeNivel)

    def nuevoLelDeNivelNoProcesado(self, unLelDeNivel: LelMmd):
        self.lelsDeNivelNoProcesados.append(unLelDeNivel)

    def nuevoLelOpcional(self, unLelDePropiedad: LelMmd):
        self.lelsArcosOpcionales.append(unLelDePropiedad)

    
    def nuevoLelMultiple(self, unLelDePropiedad: LelMmd):
        self.lelsArcosMultiples.append(unLelDePropiedad)


    def __str__(self):
        return f'''ProcesadoEnSujeto(lelsDePropiedad={self.lelsDePropiedad}, 
                lelsDeNivel={self.lelsDeNivel},
                lelsArcosOpcionales={self.lelsArcosOpcionales},
                lelsArcosMultiples={self.lelsArcosMultiples}))'''
    

    def __str__(self):
        return f'''ProcesadoEnSujeto(lelsDePropiedad={self.lelsDePropiedad}, 
                lelsDeNivel={self.lelsDeNivel},
                lelsDeNivelNoProcesados={self.lelsDeNivelNoProcesados},
                lelsArcosOpcionales={self.lelsArcosOpcionales},
                lelsArcosMultiples={self.lelsArcosMultiples})'''
