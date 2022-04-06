"""Test module for CustomList"""

import unittest
from custom_list import CustomList


class CustomListTestCase(unittest.TestCase):
    """Main test case for CustomList"""

    def assert_list_equal(self, list1, list2):
        """Per-elemental lists comparison."""
        self.assertEqual(len(list1), len(list2))
        if len(list1) == len(list2):
            for i, j in zip(list1, list2):
                self.assertEqual(i, j)

    def test_simple_addsub(self):
        """Test addition and subtraction between CustomLists"""
        # Equal size
        cust_list_3 = CustomList([1, 2, 3])
        cust_list_3_dup = CustomList([3, 2, 1])
        self.assert_list_equal(cust_list_3 + cust_list_3_dup, [4] * 3)
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(cust_list_3_dup, [3, 2, 1])
        self.assert_list_equal(cust_list_3 - cust_list_3_dup, [-2, 0, 2])
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(cust_list_3_dup, [3, 2, 1])

        # Left longer
        cust_list_2 = CustomList([3, 1])
        self.assert_list_equal(cust_list_3 + cust_list_2, [4, 3, 3])
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(cust_list_2, [3, 1])
        self.assert_list_equal(cust_list_3 - cust_list_2, [-2, 1, 3])
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(cust_list_2, [3, 1])

        # Right longer
        self.assert_list_equal(cust_list_2 + cust_list_3, [4, 3, 3])
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(cust_list_2, [3, 1])
        self.assert_list_equal(cust_list_2 - cust_list_3, [2, -1, -3])
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(cust_list_2, [3, 1])

    def test_unobvious_addsub(self):
        """Test addition and subtraction between CustomList and regular list"""
        # Equal size
        cust_list_3 = CustomList([1, 2, 3])
        list_3 = [3, 2, 1]
        self.assert_list_equal(cust_list_3 + list_3, [4] * 3)
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(list_3 + cust_list_3, [4] * 3)
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(cust_list_3 - list_3, [-2, 0, 2])
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(list_3 - cust_list_3, [2, 0, -2])
        self.assert_list_equal(cust_list_3, [1, 2, 3])

        # Left longer
        cust_list_2 = CustomList([3, 1])
        self.assert_list_equal(list_3 + cust_list_2, [6, 3, 1])
        self.assert_list_equal(cust_list_2, [3, 1])
        self.assert_list_equal(list_3 - cust_list_2, [0, 1, 1])
        self.assert_list_equal(cust_list_2, [3, 1])
        list_2 = [3, 1]
        self.assert_list_equal(cust_list_3 + list_2, [4, 3, 3])
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(cust_list_3 - list_2, [-2, 1, 3])
        self.assert_list_equal(cust_list_3, [1, 2, 3])

        # Right longer
        self.assert_list_equal(cust_list_2 + list_3, [6, 3, 1])
        self.assert_list_equal(cust_list_2, [3, 1])
        self.assert_list_equal(cust_list_2 - list_3, [0, -1, -1])
        self.assert_list_equal(cust_list_2, [3, 1])
        self.assert_list_equal(list_2 + cust_list_3, [4, 3, 3])
        self.assert_list_equal(cust_list_3, [1, 2, 3])
        self.assert_list_equal(list_2 - cust_list_3, [2, -1, -3])
        self.assert_list_equal(cust_list_3, [1, 2, 3])

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
