'''
GIL (Global Interpreter Locak) it will take care of each thread will run at time
'''

from threading import Thread
import time

class Hello(Thread):
    def run(self):
        for i in range(10):
            print('hi')
            time.sleep(3)

class Hi(Thread):
    def run(self):
        for i in range(10):
            print('hello')
            time.sleep(2)
hello = Hello()
hi = Hi()
hello.start()
time.sleep(2)
hi.start()