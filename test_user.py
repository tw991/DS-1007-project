from stockfunction import *
from datetime import datetime

def main():
    dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7), datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
    input_true_df = pd.Series([1,2,3,4,5,6], index = dates, name = 'Close')
    print sma(input_true_df,3)
    print sma(input_true_df,4)

from portfolio import *

test = portfolio(['F'])
test.simulate([1],'2010/1/1','2010/1/10')
test.end_value
if __name__ == '__main__':
    main()