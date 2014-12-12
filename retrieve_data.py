import pandas.io.data as web
import datetime


def get_data(stock, source, start, end):
    #input check
    start_year=int(start.split('/')[0])
    start_month=int(start.split('/')[1])
    start_day=int(start.split('/')[2])
    end_year=int(end.split('/')[0])
    end_month=int(end.split('/')[1])
    end_day=int(end.split('/')[2])
    start=datetime.datetime(start_year, start_month, start_day)
    end=datetime.datetime(end_year, end_month, end_day)
    # raise exception here if start==end        
    f=web.DataReader(stock, source, start, end)
    return f
    
