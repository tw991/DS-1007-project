from portfolioexception import *
import pandas as pd
import numpy as np
import datetime


def datetime_checkinput(year, month, day):
    try:
        datetime.datetime(year, month, day)
    except:
        raise Invaliddatetimeinput
    return 0


def parse_string_datetime(date):
    date_string_parse = date.split('/')
    year = int(date_string_parse[0])
    month = int(date_string_parse[1])
    day = int(date_string_parse[2])
    return year, month, day


def simulatedate_checkinput(start, end):
    start_year, start_month, start_day = parse_string_datetime(start)
    end_year, end_month, end_day = parse_string_datetime(end)
    if datetime_checkinput(start_year, start_month, start_day) == 0 and datetime_checkinput(end_year, end_month, end_day) == 0:
        start_time = datetime.datetime(start_year, start_month, start_day)
        end_time = datetime.datetime(end_year, end_month, end_day)
        if start_time < end_time:
            return 0
        else:
            raise Invaliddatetimeinput


def get_simulate_date(start, end):
    start_year, start_month, start_day = parse_string_datetime(start)
    end_year, end_month, end_day = parse_string_datetime(end)
    if simulatedate_checkinput(start, end):
        start_time = datetime.datetime(start_year, start_month, start_day)
        end_time = datetime.datetime(end_year, end_month, end_day)
        return start_time, end_time