# Imports
import concurrent.futures
from functools import reduce
from datetime import datetime

# Cria a func
def do_something(n):
    c = 0
    for i in range(n):
        #do something
        c += 1
    return c

# Reducer func
def reducer(c, c1):
    reduced = c + c1
    return reduced


# Roda o programa
if __name__ == '__main__':
    start = datetime.now()
    print(start)

    # Cria multiplos executors - processamento paralelo
    with concurrent.futures.ProcessPoolExecutor() as executor:

        # Map: applica func a lista
        mapped = executor.map(do_something, [250_000_000, 250_000_000, 250_000_000, 250_000_000])

        # reduz resultado a número único
        result = reduce(reducer, mapped)

    print(f'Result = {result: ,}. \nLead time: {datetime.now() - start}')