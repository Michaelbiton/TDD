import unittest
from src.BubbleSort import BubbleSort

class BubbleSort_test(unittest.TestCase):
    def test_return_value(self):
        # arr
        arr = [10,5,25,15,20]

        # expect/assert
        self.assertIsNotNone(BubbleSort.BubbleSort(arr))

    def test_sorting(self):
        # arr
        arr = [10,5,25,15,20]

        # assume
        expected1 = [5,10,15,20,25]

        # action
        result1 = BubbleSort.BubbleSort(arr)

        # expect/assert
        self.assertEqual(result1, expected1)

    def test_list_integrity(self):
        # arr
        arr = [10,5,25,15,20]

        # assume
        expected1 = 5

        # action
        result1 = len(BubbleSort.BubbleSort(arr))

        # expect/assert
        self.assertEqual(result1, expected1)

