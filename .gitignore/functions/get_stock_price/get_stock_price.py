#!/usr/bin/env python

import os
import sys
from datetime import datetime
from botocore.exceptions import ClientError
sys.path.append("./functions/common/")
from logger import *
from exceptions import *

LOGGER = get_logger()
TRADE_START_TIME = 10


def process_stock_price(stock_prices_today):
    LOGGER.info("Start processing yesterday's stock prices")
    if stock_prices_today and len(stock_prices_today) > 1:
        LOGGER.info("Supplied stock price list is valid. Finding max profit")
        return find_max_profit(stock_prices_today)
    else:
        LOGGER.error("Stock price not supplied: ", ValueError)
        raise ValueError


def find_max_profit(price_list):
    #TODO Find profit at the earlier stage
    #TODO Find list of profitable occurrences 
    max_profit = min_price = max_price = curr_max_price = selling_price = 0
    buying_time = selling_time =None
    try:
        for i in range(0, len(price_list)-1, 1):

            for j in range(i+1, len(price_list)):
                if (price_list[j] > price_list[i]):
                    curr_min_price = price_list[i]
                    curr_max_price = price_list[j]
                    curr_profit = price_list[j] - price_list[i]

                    if min_price == 0:
                        min_price = price_list[i]
                        buying_time = convert_into_daytime(i)
                    else:
                        min_price = min(min_price, curr_min_price)
                    if curr_min_price <=min_price:
                        buying_time = convert_into_daytime(i+1)
                    
                    max_profit = max(max_profit, curr_profit) 
                    
                    if i<j and curr_profit >= max_profit:
                        #print(max_profit)
                        selling_time = convert_into_daytime(j+1)
                        selling_price = curr_max_price

        return min_price, buying_time, selling_price, selling_time, max_profit

    except BadRequestException as e:
        LOGGER.error('BadRequest response. {}'.format(e))
        raise e
    except Exception as e:
        LOGGER.error(
            'Unexpected exception occurred... could not find min and max stock price list: {}'.format(e))
        raise e


def convert_into_daytime(transaction_minutes):
    trade_start_time = TRADE_START_TIME
    hours = 0
    if transaction_minutes > 60:
        hours = transaction_minutes/60
    minutes = transaction_minutes % 60
    trading_time = "%d:%02d:00" % (trade_start_time+hours, minutes)
    time = datetime.strptime(trading_time, "%H:%M:%S")
    time.strftime("%I:%M %p")
    return time.strftime("%I:%M %p")


#payload = [10, 7, 18, 2, 18, 3, 18]
payload0 = [10, 7, 19, 18, 2, 18, 3, 18]
payload1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
payload2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

payload3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
payload4 = [100, 90, 80, 70, 100, 60, 50, 80, 40, 30, 20, 10]
payload5 = [45, 24, 35, 31, 40, 38, 11]
payload6 = [100, 635, 180, 250, 310, 45, 535, 695]
payload7 = [10, 7, 5, 8, 11, 9]

if __name__ == "__main__":

    min_price, buying_time, max_price, selling_time, max_profit = process_stock_price(payload6)
    if max_profit != 0:
        LOGGER.info("Buy stock for a low price of : ${} at {}, Sell it when price is maximum of: ${} at {}, and make a profit of : ${}".format(
            min_price, buying_time, max_price, selling_time, max_profit))
        print("\nBuy stock for a low price of : ${} at {}, Sell stock when price is maximum of: ${} at {}, and make a profit of : ${}".format( min_price, buying_time, max_price, selling_time, max_profit))

    else:
        LOGGER.info("Couldn't make any profit as the market was down")
        print("Couldn't make any profit as the market was down")
    