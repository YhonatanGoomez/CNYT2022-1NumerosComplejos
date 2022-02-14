import CNYT
import unittest

class Test(unittest.TestCase):

    def test_Suma(self):
        sumacomp =CNYT.Suma((3, 5), (-2.6, 6.8))
        self.assertAlmostEqual(sumacomp[0], 0.4)
        self.assertAlmostEqual(sumacomp[1],  11.8)
    def test_Producto(self):
        Produccomp =CNYT.Producto((-3,-5),(7,-9))
        self.assertAlmostEqual(Produccomp[0], -66)
        self.assertAlmostEqual(Produccomp[1],  -8)
    def test_Resta(self):
        restacomp =CNYT.Resta((-2, 6), (-4, 0))
        self.assertAlmostEqual(restacomp[0], 2)
        self.assertAlmostEqual(restacomp[1],  6)
    def test_Division(self):
        Divisioncomp=CNYT.Division((-4,5),(8,-2))
        self.assertAlmostEqual(Divisioncomp[0], -0.6176470588235294)
        self.assertAlmostEqual(Divisioncomp[1],  0.47058823529411764)
    def test_Modulo(self):
        Modulocomp = CNYT.Modulo((-3,7))
        self.assertAlmostEqual(Modulocomp, 7.615773105863909)
    def test_Conjugado(self):
        Conjugadocomp = CNYT.Conjugado((-3,7))
        self.assertAlmostEqual(Conjugadocomp[0], -3)
        self.assertAlmostEqual(Conjugadocomp[1], -7)
    def test_ConversionPAC(self):
        ConverPACcomp = CNYT.ConversionPolarACartesiana(2,120)
        self.assertAlmostEqual(ConverPACcomp[0], -0.9999999999999996)
        self.assertAlmostEqual(ConverPACcomp[1], 1.7320508075688774)
    def test_ConversionCAP(self):
        ConverCAPcomp = CNYT.ConversionCartesianaAPolar(1,1.7320508075688774)
        self.assertAlmostEqual(ConverCAPcomp[0], 2.0)
        self.assertAlmostEqual(ConverCAPcomp[1], 60.00000000000001)
    def test_Fase(self):
        fasecomp = CNYT.Fase((3,4))
        self.assertAlmostEqual(fasecomp, 53.13010235415598)





if __name__ == '__main__':
    unittest.main()
