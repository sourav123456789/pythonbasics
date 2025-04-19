import time

def timer(func):
    def wrapper(*args , **kwargs):
        start_time = time.time()
        func(*args , **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time} time")
    return wrapper


