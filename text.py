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

        # ʹ�� subprocess ���� akshare_helper.py �еĹ���
        result = subprocess.run(['python', 'stock_analysis.py', 'get_stock_info', stock_code], capture_output=True)

        # ������
        if result.returncode == 0:
            print(result.stdout.decode())
        else:
            print(f"Error: {result.stderr.decode()}")
