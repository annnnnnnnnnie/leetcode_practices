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


class TestAppleShelf(unittest.TestCase):
    def setUp(self) -> None:
        self.appleShelf = Daily.src.dec24_2021.AppleShelf
        self.apple_shelf = self.appleShelf(0)

    def test_add_one_apple(self):
        self.apple_shelf.batch_add_apple(1, 1)
        apple = self.apple_shelf.try_get_one_apple()
        self.assertEqual(1, apple)

    def test_expire_one_apple(self):
        self.apple_shelf.batch_add_apple(1, 1)
        self.apple_shelf.forward_one_day()
        apple = self.apple_shelf.try_get_one_apple()
        self.assertEqual(0, apple)


class TestEatApple(unittest.TestCase):
    def setUp(self) -> None:
        self.eaten_apples = Daily.src.dec24_2021.eaten_apples

    def test_case_1(self):
        apples = [1, 2, 3, 5, 2]
        days = [3, 2, 1, 4, 2]
        result = self.eaten_apples(apples, days)
        answer = 7
        self.assertEqual(answer, result)

    def test_case_2(self):
        apples = [3, 0, 0, 0, 0, 2]
        days = [3, 0, 0, 0, 0, 2]
        result = self.eaten_apples(apples, days)
        answer = 5
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
