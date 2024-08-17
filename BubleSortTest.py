import unittest
import BubleSort

class TestBubleSort(unittest.TestCase):
    def test_sort(self):
        obj = BubleSort.BubleSort()
        self.assertEqual(obj.sort([8,2,5,6]),[2,5,6,8])
        self.assertEqual(obj.sort([]),[])
        self.assertEqual(obj.sort([100]),[100])

unittest.main()