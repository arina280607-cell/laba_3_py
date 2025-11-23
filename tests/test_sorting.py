from src.sorting import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort
import unittest

class TestSortingAlgorithms(unittest.TestCase):

    def test_bubble_sort_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_bubble_sort_single(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_bubble_sort_all_same(self):
        self.assertEqual(bubble_sort([3, 3, 3, 3]), [3, 3, 3, 3])

    def test_bubble_sort_ascending(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_bubble_sort_descending(self):
        self.assertEqual(bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_bubble_sort_random(self):
        self.assertEqual(bubble_sort([3, 1, 4, 2]), [1, 2, 3, 4])

    def test_quick_sort_empty(self):
        self.assertEqual(quick_sort([]), [])

    def test_quick_sort_single(self):
        self.assertEqual(quick_sort([1]), [1])

    def test_quick_sort_all_same(self):
        self.assertEqual(quick_sort([5, 5, 5]), [5, 5, 5])

    def test_quick_sort_ascending(self):
        self.assertEqual(quick_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_quick_sort_descending(self):
        self.assertEqual(quick_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_quick_sort_random(self):
        self.assertEqual(quick_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])

    def test_counting_sort_empty(self):
        self.assertEqual(counting_sort([]), [])

    def test_counting_sort_single(self):
        self.assertEqual(counting_sort([1]), [1])

    def test_counting_sort_all_same(self):
        self.assertEqual(counting_sort([2, 2, 2, 2]), [2, 2, 2, 2])

    def test_counting_sort_ascending(self):
        self.assertEqual(counting_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_counting_sort_descending(self):
        self.assertEqual(counting_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_counting_sort_with_negative(self):
        self.assertEqual(counting_sort([-1, -3, 0, 2, -1]), [-3, -1, -1, 0, 2])

    def test_radix_sort_empty(self):
        self.assertEqual(radix_sort([]), [])

    def test_radix_sort_single(self):
        self.assertEqual(radix_sort([5]), [5])

    def test_radix_sort_all_same(self):
        self.assertEqual(radix_sort([7, 7, 7]), [7, 7, 7])

    def test_radix_sort_ascending(self):
        self.assertEqual(radix_sort([10, 20, 30, 40]), [10, 20, 30, 40])

    def test_radix_sort_descending(self):
        self.assertEqual(radix_sort([40, 30, 20, 10]), [10, 20, 30, 40])

    def test_radix_sort_mixed(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]),
                         [2, 24, 45, 66, 75, 90, 170, 802])

    def test_radix_sort_negative_raises(self):
        with self.assertRaises(ValueError):
            radix_sort([-1, 2, 3])

    def test_bucket_sort_empty(self):
        self.assertEqual(bucket_sort([]), [])

    def test_bucket_sort_single(self):
        self.assertEqual(bucket_sort([0.5]), [0.5])

    def test_bucket_sort_all_same(self):
        self.assertEqual(bucket_sort([0.3, 0.3, 0.3]), [0.3, 0.3, 0.3])

    def test_bucket_sort_ascending(self):
        self.assertEqual(bucket_sort([0.1, 0.2, 0.3, 0.4]), [0.1, 0.2, 0.3, 0.4])

    def test_bucket_sort_descending(self):
        self.assertEqual(bucket_sort([0.9, 0.8, 0.7, 0.6]), [0.6, 0.7, 0.8, 0.9])

    def test_bucket_sort_mixed(self):
        self.assertEqual(bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]),
                         [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897])

    def test_heap_sort_empty(self):
        self.assertEqual(heap_sort([]), [])

    def test_heap_sort_single(self):
        self.assertEqual(heap_sort([42]), [42])

    def test_heap_sort_all_same(self):
        self.assertEqual(heap_sort([9, 9, 9, 9]), [9, 9, 9, 9])

    def test_heap_sort_ascending(self):
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_heap_sort_descending(self):
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_heap_sort_random(self):
        self.assertEqual(heap_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])


