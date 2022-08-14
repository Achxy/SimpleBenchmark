from time import sleep

from simplebenchmark.api import sync_benchmark


@sync_benchmark()
def foo(some_arg: int):
    sleep(0.5)
    print("Hey!", some_arg)
    return "Okay!"


foo(9)
print(repr(foo))
