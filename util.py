import time
from functools import wraps


def benchmark(f):
    @wraps(f)
    def run(*args, **kwargs):
        t1 = time.perf_counter()
        result = f(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{f.__name__} completed in {(t2 - t1) * (10 ** 9)} nano seconds")
        return result

    return run
