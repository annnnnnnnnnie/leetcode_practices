import unittest

import Daily.src.dec21_2021


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.is_leap_year = Daily.src.dec21_2021.is_leap_year
        self.days_in_a_month = Daily.src.dec21_2021.compute_days_in_month
        self.date_in_a_year = Daily.src.dec21_2021.compute_date_of_year
        self.day_of_year = Daily.src.dec21_2021.day_of_year

    def test_2020_is_leap_year(self):
        year = 2020
        result = self.is_leap_year(year)
        self.assertTrue(result)

    def test_2021_is_not_leap_year(self):
        year = 2021
        result = self.is_leap_year(year)
        self.assertFalse(result)

    def test_2100_is_not_leap_year(self):
        year = 2100
        result = self.is_leap_year(year)
        self.assertFalse(result)

    def test_2000_is_leap_year(self):
        year = 2000
        result = self.is_leap_year(year)
        self.assertTrue(result)

    def test_jan_in_2020_31_days(self):
        year = 2020
        month = 1
        result = self.days_in_a_month(month, year)
        answer = 31
        self.assertEqual(answer, result)

    def test_feb_in_2020_29_days(self):
        year = 2020
        month = 2
        result = self.days_in_a_month(month, year)
        answer = 29
        self.assertEqual(answer, result)

    def test_feb_in_2100_28_days(self):
        year = 2100
        month = 2
        result = self.days_in_a_month(month, year)
        answer = 28
        self.assertEqual(answer, result)

    def test_jan_1_is_day_one(self):
        year = 2020
        month = 1
        day = 1
        result = self.date_in_a_year(year, month, day)
        answer = 1
        self.assertEqual(answer, result)

    def test_2021_dec_31_is_day_365(self):
        year = 2021
        month = 12
        day = 31
        result = self.date_in_a_year(year, month, day)
        answer = 365
        self.assertEqual(answer, result)

    def test_2020_mar_1_is_day_61(self):
        year = 2020
        month = 3
        day = 1
        result = self.date_in_a_year(year, month, day)
        answer = 61
        self.assertEqual(answer, result)

    def test_case_1(self):
        date = "2019-01-09"
        result = self.day_of_year(date)
        answer = 9
        self.assertEqual(answer, result)

    def test_case_2(self):
        date = "2019-02-10"
        result = self.day_of_year(date)
        answer = 41
        self.assertEqual(answer, result)

    def test_case_3(self):
        date = "2003-03-01"
        result = self.day_of_year(date)
        answer = 60
        self.assertEqual(answer, result)

    def test_case_4(self):
        date = "2004-03-01"
        result = self.day_of_year(date)
        answer = 61
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
