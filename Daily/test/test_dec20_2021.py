import unittest
import Daily.src.dec20_2021


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.find_radius = Daily.src.dec20_2021.find_radius

    def test_case_1(self):
        houses = [1, 2, 3]
        heaters = [2]
        result = self.find_radius(houses, heaters)
        answer = 1
        self.assertEqual(answer, result)

    def test_case_2(self):
        houses = [1, 2, 3, 4]
        heaters = [1, 4]
        result = self.find_radius(houses, heaters)
        answer = 1
        self.assertEqual(answer, result)

    def test_case_3(self):
        houses = [1, 5]
        heaters = [2]
        result = self.find_radius(houses, heaters)
        answer = 3
        self.assertEqual(answer, result)

    def test_not_in_order_heaters(self):
        houses = [1, 2, 3, 4, 5]
        heaters = [4, 2]
        result = self.find_radius(houses, heaters)
        answer = 1
        self.assertEqual(answer, result)

    def test_complicated_case(self):
        houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        heaters = [3, 7, 12]
        result = self.find_radius(houses, heaters)
        answer = 2
        self.assertEqual(answer, result)

    def test_complicated_case_2(self):
        houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        heaters = [3, 7, 15]
        result = self.find_radius(houses, heaters)
        answer = 3
        self.assertEqual(answer, result)

    def test_complicated_case_3(self):
        houses = [1, 2, 3, 5, 15]
        heaters = [2, 30]
        result = self.find_radius(houses, heaters)
        answer = 13
        self.assertEqual(answer, result)


class TestFindNearestHeater(unittest.TestCase):
    def setUp(self) -> None:
        self.find_nearest_heater = Daily.src.dec20_2021.find_nearest_heater

    def test_find_heater_overlapped(self):
        house_position = 2
        heaters = [1, 2, 3, 4]
        result = self.find_nearest_heater(house_position, heaters, 0)
        answer = (1, 0)
        self.assertTupleEqual(answer, result)

    def test_find_heater_similar(self):
        house_position = 3
        heaters = [1, 4]
        result = self.find_nearest_heater(house_position, heaters, 0)
        answer = (1, 1)
        self.assertTupleEqual(answer, result)

    def test_find_heater_far_away(self):
        house_position = 1
        heaters = [499, 500, 501]
        result = self.find_nearest_heater(house_position, heaters, 0)
        answer = (0, 498)
        self.assertTupleEqual(answer, result)

    def test_find_heater_closer_closer(self):
        house_position = 502
        heaters = [499, 500, 501, 502, 503]
        result = self.find_nearest_heater(house_position, heaters, 0)
        answer = (3, 0)
        self.assertTupleEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
