import datetime
import time
import requests
import concurrent.futures
import akshare as ak
import pandas as pd
import sys
akshare_path = 'F:/python/akshare/.venv/Lib/site-packages'
sys.path.insert(0, akshare_path)

# 全局配置参数
PERIOD = 'daily'
START_DATE = "19910101"
ADJUST = "hfq"

# 获取今日日期
today = datetime.date.today().strftime("%Y%m%d")

# 获取所有A股的股票信息
stock_info_df = ak.stock_info_a_code_name()

# 打印列名
print(stock_info_df.columns)

# 确认正确的列名
code_column_name = 'code'  # 替换成正确的列名
name_column_name = 'name'  # 替换成正确的列名

code_id_dict = dict(zip(stock_info_df[code_column_name], stock_info_df[name_column_name]))

def download_stock_data(code):
    try:
        # 检查股票代码是否在字典中
        if code not in code_id_dict:
            print(f"无法找到 {code} 对应的股票名称，跳过该股票代码的处理。")
            return None

        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period=PERIOD, start_date=START_DATE, end_date=today, adjust=ADJUST)
        data_json = stock_zh_a_hist_df.to_dict(orient='records')

        if not data_json:
            print(f"No data available for {code} within the specified date range.")
            return None

        stock_zh_a_hist_df.to_csv(".\\%s.csv" % code, index=False)
        print(f"完成{code}的数据下载！")
        return code
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON 解析失败: {e}")
        return None


if __name__ == "__main__":
    # 获取所有股票代码
    stock_names_df = ak.stock_info_a_code_name()

    # 确认正确的列名
    stock_names_column_name = 'code'  # 替换成正确的列名
    stock_names = stock_names_df[stock_names_column_name].tolist()

    # 设置并发线程数，可以根据需求调整
    max_workers = 200  # 替换成你想要的线程数

    millisecondsStart = int(round(time.time()))

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(download_stock_data, stock_names)

    # 处理结果
    successful_downloads = [result for result in results if result is not None]
    print(f"成功下载的股票数量: {len(successful_downloads)}")

    millisecondsEnd = int(round(time.time()))
    print(f"全部完成共耗时：{(millisecondsEnd - millisecondsStart)}秒")