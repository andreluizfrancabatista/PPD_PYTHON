# Imports
import concurrent.futures
from functools import reduce
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
    # creating multiple executor - Parallel processing
    with concurrent.futures.ProcessPoolExecutor() as executor:

        # Map: aplica função a lista
        mapped = executor.map(do_something, [500_000_000, 500_000_000])


    print(f'mapped = {list(mapped)}. \nLead time: {datetime.now() - start}')