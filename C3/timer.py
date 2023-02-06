import os
from time import sleep


def timer(start = 10, stop = 0, message = 'time elapsed'):
    while start != stop-1:
        os.system('cls||clear')
        print(start)
        sleep(1)
        start -=1
    if message:
        print(message)
    

if __name__ == "__main__":
    timer(20, 10, "that's all")