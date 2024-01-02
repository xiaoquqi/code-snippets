import logging

def my_function(verbose=False):
    # 创建一个logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # 创建一个输出到文件的handler
    file_handler = logging.FileHandler('my_log.log')
    file_handler.setLevel(logging.DEBUG)

    # 创建一个格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 将格式化器应用到handler
    file_handler.setFormatter(formatter)

    # 添加handler到logger
    logger.addHandler(file_handler)

    # 输出日志
    if verbose:
        # 创建一个输出到标准输出的handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        logger.debug('This is a debug message.')
        logger.info('This is an info message.')
    else:
        logger.warning('This is a warning message.')
        logger.error('This is an error message.')

# 调用函数
my_function(verbose=True)
