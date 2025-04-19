from time import sleep
from Dacorator.timer.Timming_execution_function import timer

@timer
def example(n):
    sleep(n)
    print("executed example function")

example(3)
