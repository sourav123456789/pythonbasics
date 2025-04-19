def cache(func):
    my_dict = { }

    def wrapper(*args):
        print("inside cache")
        for k, v in my_dict.items( ):
            print(f"key is {k} value is {v}")
        if args in my_dict:
            return my_dict[args]
        res = func(*args)
        my_dict[args] = res
        return res

    return wrapper
