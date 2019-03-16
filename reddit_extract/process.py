import multiprocessing
from multiprocessing.pool import ThreadPool

class MultiProcess(object):

    def __init__(self, threads):
        """
        Args:
            threads: number of threads to use
        """
        self.threads = threads
        self.pool = ThreadPool(threads)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Dispose
        """
        self.pool.join()

    def process(self, operation, items):
        result = self.pool.starmap(operation, items) # multi-args starmap
        self.pool.close()
        return result
