"""Test module for CustomList"""

import unittest
from custom_list import CustomList


class CustomListTestCase(unittest.TestCase):
    """Main test case for CustomList"""

    def test_simple_addsub(self):
        """Test addition and subtraction between CustomLists"""
        temp = CustomList([5, 1, 3, 7])
        check = temp - CustomList([1, 2, 7])
        self.assertListEqual(temp, CustomList([5, 1, 3, 7]))
        expect = CustomList([4, -1, -4, 7])
        self.assertListEqual(check, expect)
        check = CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])
        expect = CustomList([6, 3, 10, 7])
        self.assertListEqual(check, expect)

    def test_unobvious_addsub(self):
        """Test addition and subtraction between CustomList and regular list"""
        check = [1, 2] + CustomList([3, 4])
        expect = CustomList([4, 6])
        self.assertListEqual(check, expect)
        check = [1, 2] - CustomList([3, 4])
        expect = CustomList([-2, -2])
        self.assertListEqual(check, expect)
        check = CustomList([3, 4]) + [1, 2]
        expect = CustomList([4, 6])
        self.assertListEqual(check, expect)
        check = CustomList([3, 4]) - [1, 2]
        expect = CustomList([2, 2])
        self.assertListEqual(check, expect)

    def test_equality(self):
        """Test equality of CustomLists"""
        self.assertEqual(CustomList([5, 1, -3, 7]), CustomList([1, 2, 7]))
        self.assertEqual(CustomList([1, 2, 3]), CustomList([3, 2, 1]))
        self.assertGreater(CustomList([10, 5]), [11, 0])
        self.assertLess([9], CustomList([3, 3, 3, 3]))
        self.assertLessEqual([9], CustomList([3, 3, 3]))
        self.assertGreaterEqual(CustomList([1]), [1, -2, 2])
        self.assertNotEqual(CustomList([1, 2, 3]), CustomList([1, 2, 3, -3]))
        self.assertGreater(CustomList([1.0, 2.0, 3.0]),
                           CustomList([1.0, 2.0, 3.0, -3.0]))

    def test_str(self):
        """Test __str__ method of CustomList"""
        self.assertEqual(str(CustomList([1, 2, 3, 4, 5])), "[1, 2, 3, 4, 5] sum=15")
        self.assertEqual(str(CustomList()), "[] sum=0")
        self.assertEqual(str(CustomList([-1])), "[-1] sum=-1")
        self.assertEqual(str(CustomList([2.0])), "[2.0] sum=2.0")


if __name__ == "__main__":
    unittest.main()
