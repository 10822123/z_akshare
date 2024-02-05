import cmd2
import subprocess


class AkshareCommands(cmd2.Cmd):
    def do_get_stock_info(self, line):
        """
        Get stock information using akshare.
        Usage: get_stock_info <stock_code>
        Example: get_stock_info sz000001
        """
        stock_code = line.strip()

        # 使用 subprocess 调用 akshare_helper.py 中的功能
        result = subprocess.run(['python', 'stock_analysis.py', 'get_stock_info', stock_code], capture_output=True)

        # 处理结果
        if result.returncode == 0:
            print(result.stdout.decode())
        else:
            print(f"Error: {result.stderr.decode()}")
