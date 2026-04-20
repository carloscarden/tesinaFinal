from enum import Enum


class TipoLinkDiagrama(Enum):
    ARCO_MULTIPLE ='linkNormal'
    ARCO_OPCIONAL = 'linkOpcional'
    ARCO_HECHO = 'linkNormal'
    ARCO_DIMENSION = 'linkNormal'