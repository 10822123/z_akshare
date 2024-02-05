import akshare as ak

def get_stock_info(stock_code):
    """
    Get stock information using akshare.
    """
    stock_info = ak.stock_zh_a_daily(symbol=stock_code, adjust="qfq")
    return stock_info
