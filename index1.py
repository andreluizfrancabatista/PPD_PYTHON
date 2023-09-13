#Imports
from datetime import datetime


def do_something(n):
    c = 0
    for i in range(n):
        #do something
        c += 1
    return c
if __name__ == '__main__':
    start = datetime.now()
    print(start)

    result = do_something(1_000_000_000)

    print(f'c = {result:,}. \nLead time: {datetime.now() - start}')