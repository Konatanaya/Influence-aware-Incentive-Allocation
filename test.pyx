import time

def say_hello():
    sum = 0
    t = time.time()
    for i in range(100000):
        for j in range(100000):
            sum = i*j
    print(time.time()-t)
