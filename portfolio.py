from stockfunction import *
from portfoliofunction import *
from stockexception import *
import datetime



def stock_ticker_to_instance(stock_ticker_list):
    stock_list = [stock(x) for x in stock_ticker_list] # use stock class to create stock instance for each ticker
    return stock_list


class portfolio():

    def __init__(self, stock_ticker_list, starting_cash = 10000):
        self.stock_ticker_list = stock_ticker_list
        self.stock_list = stock_ticker_to_instance(stock_ticker_list)
        self.start_value = float(starting_cash)
        self.end_value = 0
        self.position = False
        self.start_time = False
        self.end_time = False

    def _position_checkinput(self, position_list, ticker_list):
        if len(position_list) != len(ticker_list):
            raise Invalidposition
        if np.sum(position_list) > self.start_value:
            raise Invalidposition
        return 0

    def _set_simulatetime(self, start, end):
        self.start_time, self.end_time = get_simulate_date(start, end)

    def set_position(self, position_list):
        """
        allocate the investment money to all chosen stock
        """
        if self._position_checkinput(position_list, self.stock_ticker_list) == 0:
            self.position = pd.DataFrame(position_list, index = self.stock_ticker_list)

    def simulate(self, start, end):
        """
        start and ending_time are strings. year/month/day
        """
        if not self.position:
            raise Undefinedposition
        else:
            position = self.position
        self._set_simulatetime(start, end)
        start_price_list = pd.DataFrame([stock['Close'].ix[self.start_time] for stock in self.stock_list], index = self.stock_ticker_list)
        end_price_list = pd.DataFrame([stock['Close'].ix[self.end_time] for stock in self.stock_list], index = self.stock_ticker_list)
        share_list = self.position/start_price_list
        end_value_list = share_list*end_price_list
        self.end_value = float(end_value_list.sum())







