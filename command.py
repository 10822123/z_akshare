import cmd2
import logging

from pyfiglet import Figlet
from colorama import init, Fore
from config.command import config_command

from command.demo1 import demo1
from command.demo2 import demo2
from command.akshare import Akshares

# alias: 用于创建和管理命令别名。
# hello: 一个简单的示例命令，用于向用户打招呼。
# history: 显示或操作命令历史记录。
# quit: 退出交互式应用程序。
# run_script: 运行来自文件的脚本。
# shell: 在子shell中运行系统命令。
# sum: 一个简单的示例命令，用于计算一组数字的总和。
# edit: 打开编辑器以编辑多行命令。
# help: 显示帮助信息。
# macro: 创建和管理宏，它们是一组命令的集合。
# run_pyscript: 运行来自 Python 脚本的命令。
# set: 设置或显示配置变量。
# shortcuts: 显示和管理键盘快捷方式。
# 这些命令提供了一些方便的功能，使得

class MyCmdApp(Akshares,demo1, demo2):
    def __init__(self):
        super().__init__()

        # 配置隐藏命令
        if not config_command.show_hidden_commands:
            # 配置是否显示隐藏命令
            self.hidden_commands.extend(config_command.hidden_commands)

        # 修改命令提示符
        self.prompt = config_command.prompt
        # 配置是否显示命令执行时间
        self.timing = config_command.show_timing

        if config_command.enable_logging:
            self.log_file = config_command.log_file_path
            self.log_format = config_command.log_format
            self.log_level = config_command.log_level
            logging.basicConfig(filename=self.log_file, level=self.log_level, format=self.log_format)

    def generate_large_colored_art(self, text, color):
        """生成大字体彩色字符图案."""
        f = Figlet(font='slant')
        large_art = f.renderText(text)
        colored_art = f"{color}{large_art}{Fore.RESET}"
        return colored_art

    def preloop(self):
        """在命令循环开始时执行，显示欢迎消息."""
        print("===== Welcome Command Prompt =====")
        init(autoreset=True)
        large_colored_text = self.generate_large_colored_art("Hello , World !", Fore.GREEN)
        print(large_colored_text)

    def default(self, statement):
        """默认处理未识别命令的方法."""
        unknown_cmd = statement.command
        self.poutput(f'"{unknown_cmd}" 不是一个已识别的命令或别名。')
        return False  # 返回 False 表示不停止继续循环

    def do_edit(self, args):
        """打开编辑器以编辑多行命令。"""
        # 实现编辑命令的逻辑
        pass

    def do_help(self, arg):
        """帮助命令。Usage: help [command]

        参数：
        - command: 要获取帮助的命令。如果未提供，将显示所有命令的帮助。

        示例：
        > help hello
        显示 hello 命令的帮助信息。
        """
        if arg:
            # 如果提供了命令名，显示该命令的详细帮助信息
            self.show_command_help(arg)
        else:
            # 如果未提供命令名，显示所有命令的简要帮助信息
            self.show_all_commands_help()

    def show_command_help(self, command):
        """显示特定命令的帮助信息"""
        if command in self.get_all_commands():
            self.poutput(f"帮助信息 for {command}:")
            docstring = getattr(self, f"do_{command}").__doc__
            self.poutput(docstring)
        else:
            self.poutput(f"未找到命令 {command}")

    def show_all_commands_help(self):
        """显示所有命令的简要帮助信息"""
        self.poutput("可用的命令:")
        for command in self.get_all_commands():
            docstring = getattr(self, f"do_{command}").__doc__
            short_description = docstring.splitlines()[0] if docstring else "无说明"
            self.poutput(f"{command}: {short_description}")

    def do_history(self, arg):
        """显示或操作命令历史记录命令。"""
        history = self.history
        self.poutput("Command History:")
        for i, cmd in enumerate(history, start=1):
            self.poutput(f"{i}. {cmd}")

    def do_exit(self, arg):
        """退出应用程序命令。"""
        large_colored_text = self.generate_large_colored_art("Goodbye !", Fore.GREEN)
        print(large_colored_text)
        return True

    def do_quit(self, args):
        """退出应用程序命令。"""
        large_colored_text = self.generate_large_colored_art("Goodbye !", Fore.GREEN)
        print(large_colored_text)
        return True

    def postcmd(self, stop, statement):
        """命令执行后的回调函数."""
        logging.info(f'执行的命令: "{statement.raw}"')
        return stop


if __name__ == '__main__':
    app = MyCmdApp()
    try:
        app.cmdloop(intro='Welcome to MyCmdApp. Type help or ? to list command.\n')
    except KeyboardInterrupt:
        large_colored_text = app.generate_large_colored_art("Goodbye !", Fore.GREEN)
        print(large_colored_text)