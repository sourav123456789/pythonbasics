def debug(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("printing the **args and **KWargs")
        for arg in args:
            print(arg)
        for k, v in kwargs.items( ):
            print(k, v)

    return wrapper
