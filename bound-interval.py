"""bound-interval - simple class to schedule a job every n seconds for x minutes 

"""
import time
from typing import Callable, Any

class BoundInterval():
    '''BoundInterval - schedule processes to run n times for x minutes
    '''

    def __init__(self, tf_minutes: float = 60, interval_seconds: float = 20):
        self.tf_seconds = tf_minutes * 60
        self.interval_seconds = interval_seconds

    def scan(self, tf_minutes: float = 60):
        runs = 0
        start = time.time()
        while True:
            now = time.time()
            if now - start <= self.tf_seconds:
                print(now - start)
                time.sleep(self.interval_seconds)
                runs +=1
                print(runs)
            else:
                print("Exiting")
                return
              
    def test(self):
        self.scan()

def main():
    bd = BoundInterval(.2, 1)
    bd.scan()

if __name__ == "__main__":
    main()
