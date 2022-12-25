import time

print(time.time())


def speed_decorator(function):
    """
    decorator to measure the speed of running a funtion
    """
    def wrapper_function():
        print(f'running {function.__name__}')
        start_time = time.time()
        function()
        print(f'took {time.time() - start_time} seconds to run the funtion')
    return wrapper_function

@speed_decorator
def fast_function():
    for i in range(10000000):
        i*i

@speed_decorator
def slow_funtion():
    for i in range(100000000):
        i*i


fast_function()
slow_funtion()