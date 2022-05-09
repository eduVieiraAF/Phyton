
# It's a thread that runs in the background, not important for our program to run



import imp
import threading
import time

def timer():
    print()
    count = 0
    
    while True:
        time.sleep(1)
        count += 1
        print("logged in for " + str(count) + " secs")

x = threading.Thread(target = timer, daemon = True)
x.start()

user_input = input("Type anything: ")