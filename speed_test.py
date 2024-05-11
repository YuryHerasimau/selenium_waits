from functools import wraps
from datetime import datetime


def speed_test(func):
    # @wraps allows accessing the properties of the decorated function from the decorator
    @wraps(func)
    def wrapper(**args):
        start = datetime.now()
        func(**args)
        end = datetime.now()
        # Convert execution time to milliseconds
        time_delta = (end - start).total_seconds() * 1000
        # Round to seconds and 2 decimal places
        rounded_time_delta = round(time_delta/1000, 2) 
        print(f'{func.__name__} function runs in {rounded_time_delta} seconds.')

    return wrapper