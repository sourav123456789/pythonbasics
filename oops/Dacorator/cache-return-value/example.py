import time
from cache import cache


@cache
def long_running_function(a, b):
    time.sleep(10)
    return a + b


print(long_running_function(2, 3))
print("--------")
print(long_running_function(2, 3))
print("--------")
print(long_running_function(2, 5))
print("--------")
print(long_running_function(2, 5))