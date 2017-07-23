import time
from multiprocessing import Pool

import numpy as np
from progressbar import ProgressBar


def dot_if_zero(integer):
    return integer if integer != 0 else "."


def avg_and_std(values, chances):
    values = np.array(values)
    chances = np.array(chances)
    avg = np.sum(values * chances)
    std = np.sqrt(np.sum(chances * (values - avg) ** 2))
    return avg, std


def parallel_exec(func, args_iter):
    pool = Pool()
    async_results = list(map(lambda args: pool.apply_async(func, args=args), args_iter))
    pool.close()

    results = [None] * len(async_results)
    ready = [False] * len(async_results)
    bar = ProgressBar(max_value=len(async_results))
    while not all(ready):
        for i, async_result in enumerate(async_results):
            if not ready[i] and async_result.ready():
                results[i] = async_result.get()
                ready[i] = True
        bar.update(sum(ready))
        time.sleep(.5)
    pool.join()

    return results
