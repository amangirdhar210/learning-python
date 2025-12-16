import threading

def print_odd(cond, limit):
    num = 1
    with cond:
        while num <= limit:
            print(num)
            num += 2
            cond.notify()
            cond.wait()

def print_even(cond, limit):
    num = 2
    with cond:
        while num <= limit:
            cond.wait()
            print(num)
            num += 2
            cond.notify()

cond = threading.Condition()

t1 = threading.Thread(target=print_odd, args=(cond, 10))
t2 = threading.Thread(target=print_even, args=(cond, 10))

t1.start()
t2.start()

t1.join()
t2.join()
