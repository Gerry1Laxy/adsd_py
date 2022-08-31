from datetime import datetime

import numpy as np

from application.salary import calculate_salary
from application.db.people import get_employees


def avg_random(num):
    return np.sum(np.random.random(num)) / num


if __name__ == '__main__':
    print(f'Сегодня: {datetime.now().strftime("%d %B %Y")}')
    print(avg_random(100))
    calculate_salary()
    get_employees()
