#!/usr/bin/env python

import unittest
import sys
sys.path.append("./functions/get_stock_price")
sys.path.append("./functions/common/")
from get_stock_price import *


# To run test : python3 -m unittest discover -s ./tests/unit/ -p '*.py'


class TestGetStockPrice(unittest.TestCase):

    def test_convert_into_daytime_am(self):
        time = convert_into_daytime(119)
        self.assertEqual(time, "11:59 AM")

    def test_convert_into_daytime_pm(self):
        #payload = [10, 19, 7, 4,  18, 2, 18, 2, 18, 19]
        time = convert_into_daytime(121)
        self.assertEqual(time, "12:01 PM")
        # print (min_price_dict)
        # print(max_price_dict)
        # self.assertEqual(len(min_price_dict), 2)
        # self.assertEqual(len(max_price_dict), 2)
        # print(min_price_dict(0))
        # self.assertEqual(min_price_dict[len(min_price_dict)], 2)
        # self.assertEqual(max_price_dict[1], 18)
        # self.assertEqual(max_price_dict[2], 18)

    def test_process_stock_price_empty_list(self):
        payload = []
        with self.assertRaises(ValueError):
            time = process_stock_price(payload)

    def test_process_stock_price_single_value_list(self):
        payload = [10]
        with self.assertRaises(ValueError):
            time = process_stock_price(payload)

    def test_find_max_profit_price_asscending(self):
        payload = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        buying_price, buying_time, selling_price, selling_time, max_profit = find_max_profit(
            payload)
        self.assertEqual(buying_price, 10)
        self.assertEqual(buying_time, "10:01 AM")
        self.assertEqual(selling_price, 100)
        self.assertEqual(selling_time, "10:10 AM")
        self.assertEqual(max_profit, 90)

    def test_find_max_profit_price_descending(self):
        payload = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
        buying_price, buying_time, selling_price, selling_time, max_profit = find_max_profit(
            payload)
        self.assertEqual(buying_price, 0)
        self.assertEqual(buying_time, None)
        self.assertEqual(selling_price, 0)
        self.assertEqual(selling_time, None)
        self.assertEqual(max_profit, 0)

    def test_find_max_profit_price_lattitude(self):
        payload = [10, 7, 5, 8, 11, 9]
        buying_price, buying_time, selling_price, selling_time, max_profit = find_max_profit(
            payload)
        self.assertEqual(buying_price, 5)
        self.assertEqual(buying_time, "10:03 AM")
        self.assertEqual(selling_price, 11)
        self.assertEqual(selling_time, "10:05 AM")
        self.assertEqual(max_profit, 6)

    def test_find_max_profit_price_random(self):
        payload = [100, 635, 180, 250, 310, 45, 535, 695]
        buying_price, buying_time, selling_price, selling_time, max_profit = find_max_profit(
            payload)
        self.assertEqual(buying_price, 45)
        self.assertEqual(buying_time, "10:06 AM")
        self.assertEqual(selling_price, 695)
        self.assertEqual(selling_time, "10:08 AM")
        self.assertEqual(max_profit, 650)


if __name__ == '__main__':
    unittest.main()
