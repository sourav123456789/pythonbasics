from Debug import debug


@debug
def example(name, greeting = "Hello"):
    print(f"{greeting} Mr {name}")


example("sourav", greeting = "Hi")
