# stock_commands.py
import cmd2

class demo2(cmd2.Cmd):
    def do_get_stock_info(self, line):
        """获取股票信息"""
        stock_code = input("请输入股票代码：")
        self.poutput(f"正在获取股票 {stock_code} 的信息...")


    def do_hello(self, line):
        """Say hello to the user.

        Usage: hello [name]

        If a name is provided, it will greet the specified person.
        """
        if line:
            self.poutput(f"Hello, {line}!")
        else:
            self.poutput("Hello, world!")