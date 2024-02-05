import akshare as ak

# 获取所有A股的股票信息
stock_info_df = ak.stock_info_a_code_name()

# 打印列名

print(stock_info_df.columns)