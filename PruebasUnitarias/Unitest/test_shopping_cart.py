import unittest
from shopping_cart import Item,ShoppingCart,NotExistsItemsError

APPI_VERSION = 1
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 5.0)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    def tearDown(self):
        print("Metodo tearDown despues de la pruebas")

    def test_item(self):
        item = Item("Manzana",12.0)
        self.assertEqual(item.name, 'Manzana')

    def test_not_item(self):
        item = Item("Manzana",3.0)
        self.assertNotEqual(item.name,"Pan")

    def test_nombre_producto(self):
        self.assertEqual(self.jugo.name,"Jugo") #==

    def test_nombre_not_producto(self):
        self.assertNotEqual(self.pan.name,"Manzana")

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_items())

    def test_no_contiene_producto(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())

    def test_obtener_producto(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan) #is
        self.assertIsNot(item, self.jugo)

    def test_exception_sl_obtener_jugo(self):
        with self.assertRaises(NotExistsItemsError):
            self.shopping_cart.get_item(self.jugo)

    def test_total_con_u_producto(self):
        total = self.shopping_cart.total()
        self.assertGreater(total,0) # total es mayor que 0
        self.assertLess(total, self.pan.price +1.0) # Total es menor que price + 1.0
        self.assertEqual(total,self.pan.price) # Total es igual a price

    def test_codigo_pan(self):
        self.assertRegex(self.pan.code(),self.pan.name)

    def test_fail(self):
        if 2 > 3:
            self.fail("2 no es mayor que 3")

    @unittest.skip("No ejecutar")
    def test_skip(self):
        pass
    #@unittest.skipIf(APPI_VERSION < 2,"No ejecutar porque cumple el primer parametros")
    @unittest.skipUnless(APPI_VERSION > 2,"No ejecutar porque cumple el primer parametros")
    def test_pruebas_skip(self):
        pass
    def test_str_item(self):
        self.pan.__str__()


if __name__  == "__main__":
    unittest.main()
