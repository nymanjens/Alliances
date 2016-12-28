import numpy as np
import time
from progressbar import ProgressBar
from multiprocessing import Pool

dotIfZero = lambda integer: integer if integer!=0 else "."

def avgAndStd(values, chances):
    values = np.array(values)
    chances = np.array(chances)
    avg = np.sum(values*chances)
    std = np.sqrt(np.sum(chances*(values-avg)**2))
    return avg, std

def parallelExec(func, argsIter):
    pool = Pool()
    asyncResults = map(lambda args: pool.apply_async(func, args=args), argsIter)
    pool.close()
    
    results = [None]*len(asyncResults)
    ready = [False]*len(asyncResults)
    bar = ProgressBar(max_value=len(asyncResults))
    while not all(ready):
        for i, asyncResult in enumerate(asyncResults):
            if not ready[i] and asyncResult.ready():
                results[i] = asyncResult.get()
                ready[i] = True
        bar.update(sum(ready))
        time.sleep(.5)
    pool.join()
    
    return results
