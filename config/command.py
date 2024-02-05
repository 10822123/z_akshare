class config_command:
    prompt = ' Liang : '
    use_custom_prompt = True

    # 配置是否显示隐藏命令
    show_hidden_commands = False
    # 配置隐藏命令
    hidden_commands = ['alias', 'run_script', 'shell', 'macro', 'run_pyscript', 'set', 'shortcuts']

    # 配置是否启用命令历史记录
    enable_history = True

    # 配置是否显示命令执行时间
    show_timing = False

    # 配置是否启用日志记录
    enable_logging = True
    # 配置日志等级
    log_level = 'DEBUG'
    # DEBUG: 详细的调试信息，通常用于问题诊断。
    # INFO: 程序正常运行时的消息，提供信息，但不会干扰程序的正常执行。
    # WARNING(或WARN): 表示可能出现的问题，但不影响程序的正常运行。
    # ERROR: 指示出现错误，但程序仍然可以继续运行。
    # CRITICAL: 指示严重的错误，可能导致程序崩溃。
    # 配置日志文件的路径
    log_file_path = 'logs/command.txt'
    # 日志格式配置
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
