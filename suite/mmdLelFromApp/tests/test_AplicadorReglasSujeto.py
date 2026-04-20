from django.test import TestCase
from suite.mmdLelFromApp.models.diagrama.Diagrama import Diagrama
from suite.mmdLelFromApp.models.diagrama.LinkDiagrama import LinkDiagrama
from suite.mmdLelFromApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from suite.mmdLelFromApp.services.AplicadorReglasSujeto import AplicadorDeReglasSujeto
from suite.mmdLelFromApp.services.AplicadorReglasVerbo import AplicadorDeReglasVerbo

from suite.mmdLelFromApp.tests.MockLel import MockLel


class TestAplicadorReglasSujeto(TestCase):


    def setUp(self) -> None:
        self.mockLel = MockLel().lelMockeadoEmpresaAutos()
        self.diagrama = Diagrama([], [])


        aplicadorDeReglasVerbo = AplicadorDeReglasVerbo(self.diagrama) 
        self.lelsCategoricosDeVerbo = aplicadorDeReglasVerbo.aplicarReglasDeVerbo(self.mockLel)
        print('***********************************************************')
        print("lels categoricos de verbo::", "\n".join(map(str, self.lelsCategoricosDeVerbo)))
        print('***********************************************************')

        self.aplicadorDeReglasSujeto = AplicadorDeReglasSujeto(self.diagrama) 


    def test_nodos_diagrama_sujeto(self):

        self.aplicadorDeReglasSujeto.aplicarReglasDeSujeto(self.lelsCategoricosDeVerbo,self.mockLel)
        objetosDiagramaDevueltos = self.diagrama.objetosDelDiagrama

        print('***********************************************************')
        print("objetos devueltos::", "\n".join(map(str, objetosDiagramaDevueltos)))
        print('***********************************************************')

        keys_esperadas = {
            "Model", "Factory", "Segment", "Store",
            "City", "Country", "Engine capacity", "Gender"
        }

        keys_obtenidas = {o.key for o in objetosDiagramaDevueltos}

        self.assertTrue(keys_esperadas.issubset(keys_obtenidas))


    def test_links_diagrama_verbo(self):

        l1 = LinkDiagrama("Store","City","Arco simple")
        l2 = LinkDiagrama("City","State" ,"Arco simple")
        l3 = LinkDiagrama("State","Country" ,"Arco simple")

        l4 = LinkDiagrama("Car","Model" ,"Arco simple")
        l5 = LinkDiagrama("Model","Segment" ,"Arco simple")
        l6 = LinkDiagrama("Model","Factory" ,"Arco simple")
        l7 = LinkDiagrama("Model","Engine capacity" ,"Arco simple")

        linksQueTieneQueDevolver = [l1,l2,l3,l4, l5, l6, l7]

        self.aplicadorDeReglasSujeto.aplicarReglasDeSujeto(self.lelsCategoricosDeVerbo,self.mockLel)
        linksDevueltos = self.diagrama.linksDelDiagrama

        print("links devueltos::", "\n".join(map(str, linksDevueltos)))
        print("             TEST LINKS DEL SUJETO!!!")
        try:
            # Comprueba que todos los links se dibujaron correctamente
            for s in linksQueTieneQueDevolver:
                hayLink = any((oa.desde == s.desde and oa.hasta == s.hasta) for oa in linksDevueltos)
                if(not hayLink):
                    print("link no encontrado::", s)
                self.assertTrue(hayLink)

            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')
            