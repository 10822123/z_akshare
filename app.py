import datetime
import akshare as ak
import pandas as pd

# 全局配置参数
PERIOD = 'daily'
START_DATE = "19910101"
ADJUST = "hfq"

# 获取今日日期
today = datetime.date.today().strftime("%Y%m%d")

# 获取所有A股的股票信息
# stock_info_a_code_name_df = ak.stock_info_a_code_name()
# print(stock_info_a_code_name_df)



stock_share_hold_change_sse_df = ak.stock_share_hold_change_sse(symbol="600000")
print(stock_share_hold_change_sse_df)


data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)