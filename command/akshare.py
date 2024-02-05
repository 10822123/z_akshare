import cmd2
import akshare as ak


class Akshares(cmd2.Cmd):

    def do_stock_info(self, args):
        """沪深京 A 股股票代码和股票简称数据。

        Usage: stock_info

        示例：
        > stock_info
        """
        try:
            # 获取所有A股的股票信息
            stock_info_a_code_name_df = ak.stock_info_a_code_name()
            # print(stock_info_a_code_name_df)

            self.poutput(stock_info_a_code_name_df)
        except ValueError as e:
            self.poutput(f'Error: {e}')

    def do_stock_zha_hist(self, args):
        """东方财富-沪深京 A 股日频率数据; 历史数据按日频率更新, 当日收盘价请在收盘后获取。

        Usage: stock_zha_hist [code]

        示例：
        > stock_zha_hist 000001
        """
        try:
            args = args.split(maxsplit=1)
            code = args[0] if args else '000001'
            if not code:

                self.poutput('请输入股票代码')
            # 获取历史行情数据-东财
            stock_zha_hist_df = ak.stock_zh_a_hist(code)
            self.poutput(stock_zha_hist_df)
        except ValueError as e:
            self.poutput(f'Error: {e}')


    def do_stock_demo(self, args):
        """测试数据

        Usage: stock_demo [？]

        示例：
        > stock_demo
        """
        try:
            args = args.split(maxsplit=1)
            code = args[0] if args else '202304'
            if not code:
                self.poutput('请输入股票代码')
            stock_zh_index_spot_em_df = ak.stock_zh_index_spot_em(symbol="上证系列指数")
            print(stock_zh_index_spot_em_df)
        except ValueError as e:
            self.poutput(f'Error: {e}')

