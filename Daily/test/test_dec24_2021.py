import unittest
import Daily.src.dec24_2021


class TestMinHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.priority_queue = Daily.src.dec24_2021.PriorityQueue
        pass

    def test_heap_sort(self):
        a = [i for i in range(10, 0, -1)]  # [10..1]

    def test_insert_maintains_smallest(self):
        pq = self.priority_queue()
        keys = [5, 4, 3, 2, 1]
        values = [2 * k for k in keys]
        for k, v in zip(keys, values):
            pq.insert(k, v)
        min_element = pq.peek()
        answer = values[-1]
        self.assertEqual(answer, min_element.value)

    def test_empty_check_behaves(self):
        pq = self.priority_queue()
        self.assertTrue(pq.is_empty())
        pq.insert(0, 0)
        self.assertFalse(pq.is_empty())

    def test_pop_maintains_order(self):
        pq = self.priority_queue()
        keys = [5, 4, 3, 2, 1]
        values = [2 * k for k in keys]
        for k, v in zip(keys, values):
            pq.insert(k, v)
        es = []
        while not pq.is_empty():
            e = pq.pop()
            es.append(e)
        kvs = list(map(lambda e: (e.key, e.value), es))
        answer = list(zip([i + 1 for i in range(5)], [2 * (i + 1) for i in range(5)]))
        self.assertListEqual(answer, kvs)

    def test_pop_same_order_irrespective_of_insert(self):
        pq = self.priority_queue()
        keys = [1, 2, 3, 4, 5]
        values = [3 * k for k in keys]
        for k, v in zip(keys, values):
            pq.insert(k, v)
        es = []
        while not pq.is_empty():
            e = pq.pop()
            es.append(e)
        kvs = list(map(lambda e: (e.key, e.value), es))
        answer = list(zip([i + 1 for i in range(5)], [3 * (i + 1) for i in range(5)]))
        self.assertListEqual(answer, kvs)


if __name__ == '__main__':
    unittest.main()
