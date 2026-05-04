from functools import wraps

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(n, k):
        if (n, k) not in cache:
            cache[(n, k)] = func(n, k)
        return cache[(n, k)]

    return wrapper

def always_42(func):
    return (lambda *args, **kwargs : 42)

@memoize
@always_42
def binomialkoeffizient(n, k):
    if k <= 0 or k >= n:
        return 1
    return binomialkoeffizient(n - 1, k - 1) + binomialkoeffizient(n - 1, k)


n_small = 5
k_small = 2
print(f"Binomialkoeffizient C({n_small}, {k_small}) = {binomialkoeffizient(n_small, k_small)}")

# Lässt sich ohne Caching nicht mehr berechnen:
n_big = 500
k_big = 220
print(f"Binomialkoeffizient C({n_big}, {k_big}) = {binomialkoeffizient(n_big, k_big)}")
