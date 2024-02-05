import cmd2

class demo1(cmd2.Cmd):

    def do_command1(self, arg):
        self.poutput("Command from MyCommands1: " + arg)


    def do_sum(self, args):
        """计算数字总和命令。Usage: sum [num1] [num2] [more numbers]

        参数：
        - num1, num2, more numbers: 要计算总和的数字。

        示例：
        > sum 1 2 3 4
        总和: 10
        """
        try:
            if not args:
                raise ValueError("No numbers provided.")
            numbers = list(map(float, args.split()))
            result = sum(numbers)
            self.poutput(f'Sum: {result}')
        except ValueError as e:
            self.poutput(f'Error: {e}')


    def do_greet(self, arg):
        """Greet a user with a customizable message. Usage: greet [name] [message]

        This command greets the specified user with a customizable message.
        Example:
        > greet John How are you?
        Greeting for John: How are you?
        """
        args = arg.split(maxsplit=1)
        name = args[0] if args else 'User'
        message = args[1] if len(args) > 1 else 'Hello!'
        self.poutput(f'Greeting for {name}: {message}')