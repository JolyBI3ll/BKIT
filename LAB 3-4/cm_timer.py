from contextlib import contextmanager
import time as t

@contextmanager
def cm_timer_1():
    start = t.time()
    yield
    print("time: ",t.time()-start)

class cm_timer_2:
    def __init__(self):
        self.start = True
    def __enter__(self):
        self.start = t.time()
        return self.start
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("time: ", t.time() - self.start)

if __name__ == "__main__":
    with cm_timer_1():
        t.sleep(5.5)
    with cm_timer_2():
        t.sleep(5.5)
