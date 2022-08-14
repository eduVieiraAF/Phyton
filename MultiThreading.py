# ? A thread is a flow of execution, like a separate order of instructions.
#   Each thread takes a turn running to achieve concurrency.
#   GIL = Global interpreter Lock
#   allows only one thread to hold the control of the Python interpreter at any one time

# CPU bound = program/task spends most of its time waiting for internal events (CPU intensive) - use multiprocessing

# IO bound = program/task spends most of its time waiting for external events (user input, web scraping) - use
# multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You've eaten breakfast")


def drink_coffee():
    time.sleep(4)
    print("You've drunk your coffee")


def study():
    time.sleep(5)
    print("You've finished studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# eat_breakfast()
# drink_coffee()
# study()

x.join()  # main thread will wait til x is complete
# y.join()
# z.join()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
