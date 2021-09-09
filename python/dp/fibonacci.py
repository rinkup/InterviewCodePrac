import time
start_time = time.time()
"""
# RECURSION
def fib(n):
    if n == 0: return 1
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

print(fib(30))

# MEMOIZATION
def fib(n, cache=None):
    if n == 0: return 1
    if n == 1: return 1
    if cache is None: cache = {}
    if n in cache: return cache[n]
    result = fib(n-1, cache) + fib(n-2, cache)
    cache[n] = result
    return result

print(fib(100))

"""
#Bottoms-up aproch 
def fib(n):
    a = 1
    b = 1
    for n in range(2, n+1):
        a, b = b, a+b
    return b
print(fib(100))
print("--- %s seconds ---" % (time.time() - start_time))
