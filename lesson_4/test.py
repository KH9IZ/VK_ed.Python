import unittest
import custom_meta
import descriptors

class CustomTestCase(unittest.TestCase):

    def test_magic_methods(self):
        calls = []
        class TestClass(metaclass=custom_meta.CustomMeta):
            def __init__(self, a):
                a.append('init')
            def __eq__(self, a):
                a.append('eq')
                return True
            def __hash__(self):
                calls.append('hash')
                return 0
            def __del__(self):
                calls.append('del')
        t = TestClass(calls)
        t == calls
        hash(t)
        del t
        self.assertListEqual(calls, ['init', 'eq', 'hash', 'del'])

    def test_regular_attributes(self):
        class FunnyClass(metaclass=custom_meta.CustomMeta):
           bourbon = "whiskey"
           def get_bourbon(self):
               return self.custom_bourbon
           vodka = None
           class B52:
               coffee = True
        FunnyClass.absent = '70%'
        alcogolic = FunnyClass()
        alcogolic.beer = 'good'
        self.assertEqual(alcogolic.custom_beer, 'good')
        self.assertRaises(AttributeError, getattr, alcogolic, "beer")
        self.assertEqual(alcogolic.custom_absent, '70%')
        self.assertRaises(AttributeError, getattr, alcogolic, 'absent')
        self.assertRaises(AttributeError, getattr, FunnyClass, 'absent')
        self.assertEqual(FunnyClass.custom_absent, '70%')
        self.assertEqual(alcogolic.custom_vodka, None)
        self.assertEqual(alcogolic.custom_get_bourbon(), "whiskey")
        self.assertTrue(alcogolic.custom_B52.coffee)

class DescriptorsTestCase(unittest.TestCase):

    def setUp(self):
        class Data:
            num = descriptors.Integer()
            name = descriptors.String()
            price = descriptors.PositiveInteger()
        self.d = Data()

    def test_integer(self):
        self.d.num = 1
        self.assertEqual(self.d.num, 1)
        with self.assertRaises(ValueError):
            self.d.num = "abc"
        with self.assertRaises(ValueError):
            self.d.num = 1.1
        self.d.num = True
        self.assertTrue(self.d.num)
        with self.assertRaises(ValueError):
            self.d.num = 1+1j
    
    def test_string(self):
        self.d.name = "abc"
        self.assertEqual(self.d.name, "abc")
        with self.assertRaises(ValueError):
            self.d.name = 1

    def test_positive_int(self):
        self.d.price = 1
        self.assertEqual(self.d.price, 1)
        with self.assertRaises(ValueError):
            self.d.price = "abc"
        with self.assertRaises(ValueError):
            self.d.price = 1.1
        with self.assertRaises(ValueError):
            self.d.price = 1+1j
        with self.assertRaises(ValueError):
            self.d.price = 0
        with self.assertRaises(ValueError):
            self.d.price = -1


if __name__ == "__main__":
    unittest.main()
