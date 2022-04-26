import unittest
from dataclasses import dataclass

import custom_meta
import descriptors


class CustomTestCase(unittest.TestCase):
    # pylint: disable=no-member
    def test_magic_methods(self):
        calls = []

        class TestClass(metaclass=custom_meta.CustomMeta):
            def __init__(self, val):
                val.append("init")

            def __eq__(self, val):
                val.append("eq")
                return True

            def __hash__(self):
                calls.append("hash")
                return 0

            def __del__(self):
                calls.append("del")

            def __str__(self):
                calls.append("str")
                return ""

        temp = TestClass(calls)
        self.assertTrue(temp == calls)
        self.assertEqual(str(temp), "")
        hash(temp)
        del temp
        self.assertListEqual(calls, ["init", "eq", "str", "hash", "del"])

    def test_regular_attributes(self):
        class FunnyClass(metaclass=custom_meta.CustomMeta):
            # pylint: disable=too-few-public-methods
            bourbon = "whiskey"

            def get_bourbon(self):
                return self.custom_bourbon

            vodka = None

            @dataclass
            class B52:
                coffee = True

        FunnyClass.absent = "70%"
        alcogolic = FunnyClass()
        alcogolic.beer = "good"  # pylint: disable=attribute-defined-outside-init
        self.assertEqual(alcogolic.custom_beer, "good")
        self.assertRaises(AttributeError, getattr, alcogolic, "beer")
        self.assertEqual(alcogolic.custom_absent, "70%")
        self.assertRaises(AttributeError, getattr, alcogolic, "absent")
        self.assertRaises(AttributeError, getattr, FunnyClass, "absent")
        self.assertEqual(FunnyClass.custom_absent, "70%")
        self.assertEqual(alcogolic.custom_vodka, None)
        self.assertEqual(alcogolic.custom_get_bourbon(), "whiskey")
        self.assertTrue(alcogolic.custom_B52.coffee)


class DescriptorsTestCase(unittest.TestCase):
    def setUp(self):
        @dataclass
        class Data:
            num = descriptors.Integer()
            name = descriptors.String()
            price = descriptors.PositiveInteger()

        self.data = Data()

    def test_integer(self):
        self.data.num = 1
        self.assertEqual(self.data.num, 1)
        with self.assertRaises(ValueError):
            self.data.num = "abc"
        self.assertEqual(self.data.num, 1)
        with self.assertRaises(ValueError):
            self.data.num = 1.1
        self.assertEqual(self.data.num, 1)
        self.data.num = True
        self.assertTrue(self.data.num)
        with self.assertRaises(ValueError):
            self.data.num = 1 + 1j
        self.assertEqual(self.data.num, 1)

    def test_string(self):
        self.data.name = "abc"
        self.assertEqual(self.data.name, "abc")
        with self.assertRaises(ValueError):
            self.data.name = 1
        self.assertEqual(self.data.name, "abc")

    def test_positive_int(self):
        self.data.price = 1
        self.assertEqual(self.data.price, 1)
        with self.assertRaises(ValueError):
            self.data.price = "abc"
        self.assertEqual(self.data.price, 1)
        with self.assertRaises(ValueError):
            self.data.price = 1.1
        self.assertEqual(self.data.price, 1)
        with self.assertRaises(ValueError):
            self.data.price = 1 + 1j
        self.assertEqual(self.data.price, 1)
        with self.assertRaises(ValueError):
            self.data.price = 0
        self.assertEqual(self.data.price, 1)
        with self.assertRaises(ValueError):
            self.data.price = -1
        self.assertEqual(self.data.price, 1)


if __name__ == "__main__":
    unittest.main()
