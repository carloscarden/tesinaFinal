from enum import Enum

class TipoObjetoDiagrama(Enum):
    HECHO = 'Hecho'
    MEDIDA = 'Medida'
    DIMENSION = 'NodoNormal'
    NIVEL = 'NodoNormal'
    PROPIEDAD = 'Medida'
    ARCO_OPCIONAL = 'NodoNormal'
