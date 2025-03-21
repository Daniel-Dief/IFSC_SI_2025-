import timeit

def soma(n : int):
    som = 0
    for i in range(1, n+1):
        som += i

    return som

def soma2(n : int):
    return (n * (n + 1)) // 2

def criarlista(n : int):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr

def criarlista2(n : int):
    return range(n)

timei = timeit.default_timer()
criarlista2(1000)
timef = timeit.default_timer()

print(f'Tempo: {timef - timei}')