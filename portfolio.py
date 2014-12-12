from stockfunction import *
from portfoliofunction import *
from stockexception import *
import datetime
from retrieve_data import get_data


class portfolio():
    """
    This class defines a stock investment portfolio and calculates its return over a period of time.

    Parameters:
    stock_ticker_list: list (eg. ['ADBE','F'])
        Used to specify the stocks used in portfolio

    Attributes:
    stock_ticker_list: list (eg. ['ADBE','F'])
        Used to specify the stocks used in portfolio

    start_price_list: dataframe
        Used to store the close price of all stocks in the portfolio

    end_price_list: dataframe
        Used to store the close price of all stocks in 



    """
    def __init__(self, stock_ticker_list, starting_cash = 10000):
        self.stock_ticker_list = stock_ticker_list
        self.start_price_list = []
        self.end_price_list = []
        self.start_value = float(starting_cash)
        self.end_value = 0
        self.position = False
        self.start_time = False
        self.end_time = False

    def _position_checkinput(self, position_list, ticker_list):
        if len(position_list) != len(ticker_list):
            raise Invalidposition
        if np.sum(position_list) > 1:
            raise Invalidposition
        return 0

    def _get_portfolio_data(self):
        for stock in self.stock_ticker_list:
            temp_data = get_data(stock, 'yahoo', '%d/%d/%d' %(self.start_time.year, self.start_time.month, self.start_time.day), '%d/%d/%d' %(self.end_time.year, self.end_time.month, self.end_time.day))
            start_data = temp_data['Close'].ix[0]
            end_data = temp_data['Close'].ix[len(temp_data)-1]
            self.start_price_list.append(start_data)
            self.end_price_list.append(end_data)
        self.start_price_list = pd.DataFrame(self.start_price_list, index = self.stock_ticker_list)
        self.end_price_list = pd.DataFrame(self.end_price_list, index = self.stock_ticker_list)

    def _set_simulatetime(self, start, end):
        self.start_time, self.end_time = get_simulate_date(start, end)

    def set_position(self, position_list):
        """
        Allocate the investment money to all chosen stock
        It takes in position_list as a float list with summation less or equal to 1. eg: [0.2, 0.8]
        """
        if self._position_checkinput(position_list, self.stock_ticker_list) == 0:
            self.position = pd.DataFrame(position_list, index = self.stock_ticker_list)

    def simulate(self, start, end):
        """
        start and end are strings. year/month/day
        """
        if not len(self.position):
            raise Undefinedposition
        self._set_simulatetime(start, end)
        self._get_portfolio_data()
        share_list = (self.position * self.start_value)/self.start_price_list
        end_value_list = share_list*self.end_price_list
        self.end_value = float(end_value_list.sum())






