import os
from datetime import datetime


file_dir = os.getcwd()


def logger(file_path):
    def logger_(outer_func):
        def inner_func(*args, **kwargs):
            result = outer_func(*args, **kwargs)
            file_name = 'func_logger.log'
            log_file = os.path.join(file_path, file_name)
            with open(log_file, 'a') as f:
                f.write(f'{datetime.now()}, {outer_func.__name__}: '
                        f'args - {args}, kwargs - {kwargs}, '
                        f'result - {result}\n')
            return result
        return inner_func
    return logger_


@logger(file_dir)
def summa(a, b):
    return a + b


def main():
    print(summa(1, 3))


if __name__ == '__main__':
    main()
