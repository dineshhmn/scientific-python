import numpy as np
import matplotlib.pyplot as plt

import time

def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.4f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time


def monte_carlo_sampling(data):
    number_samples = 50
    number_of_events = range(25000)
    sample_mean = []
    for x in number_of_events:
        sample_mean.append(np.mean(np.random.choice(data, number_samples)))
    return sample_mean

@timeit
def start_job():
    genrtr = np.random.default_rng()
    data = genrtr.exponential(size=2500000)
    print(len(data)/100)
    # numpy selector
    #plt_sample_unsrtd = data[::1000]
    # list selector
    plt_sample_unsrtd = [data[x] for x in range(int(len(data)/100))]
    mean_sample = np.mean(plt_sample_unsrtd)
    ms = np.empty(25000)
    ms.fill(mean_sample)
    plt.plot(plt_sample_unsrtd, label="Unsorted Data")
    plt_sample_unsrtd.sort()
    plt.plot(plt_sample_unsrtd, label='Sorted Data')
    sam_mean = monte_carlo_sampling(data)
    plt.plot(sam_mean, label='MS Sample Mean')
    plt.plot(range(25000), ms, label='Sample Mean')
    plt.legend()
    plt.show()
    plt.hist(sam_mean, bins=20)
    plt.show()



if __name__ == "__main__":
    start_job()
