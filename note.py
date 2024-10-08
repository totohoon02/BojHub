import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper


@timer
def that_a_lot_of_time():
    for i in range(100022000):
        continue


that_a_lot_of_time()
