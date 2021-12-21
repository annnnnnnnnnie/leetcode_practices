def day_of_year(date):
    yyyymmdd = date.split("-")
    year = int(yyyymmdd[0])
    month = int(yyyymmdd[1])
    day = int(yyyymmdd[2])
    return compute_date_of_year(year, month, day)


def compute_date_of_year(year, month, day):
    date = 0
    for m in range(1, month):
        date += compute_days_in_month(m, year)
    date += day
    return date


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def compute_days_in_month(month, year):
    days_in_months = {1: 31,
                      2: 28,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31}
    if month == 2 and is_leap_year(year):
        return days_in_months[month] + 1
    else:
        return days_in_months[month]


class Solution:
    def dayOfYear(self, date: str) -> int:
        return day_of_year(date)
