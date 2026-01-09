"""bound-interval - simple class to schedule a job every n seconds for x minutes 

"""
import time 
from typing import Callable, Any


def test_call():
    print("testing testing")
    return

class BoundInterval():
    '''BoundInterval - schedule processes to run n times for x minutes
    '''

    def __init__(self, fun: Callable[[], Any], tf_minutes: float = 60, interval_seconds: float = 20):
        self.tf_seconds = tf_minutes * 60
        self.interval_seconds = interval_seconds
        self.sched_call = fun

    def scan(self, tf_minutes: float = 60):
        runs = 0 
        start = time.time()
        while True:
            now = time.time()
            if now - start <= self.tf_seconds:
                print(now - start)
                self.sched_call()
                time.sleep(self.interval_seconds)
                runs +=1
                
            else:
                print("Exiting")
                return 
            

    def test(self):
        self.scan()

def main():
    bd = BoundInterval(test_call, .2, 1)
    bd.scan()

if __name__ == "__main__":
    main()
