from collections import deque
import time


class Queue:
    def __init__(self, name):
        self.name = name
        self.items = deque()

    def enqueue(self, fn):
        print(f"[ENQUEUE → {self.name}] {fn.__name__}")
        self.items.append(fn)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return not self.items



call_stack = []
macrotask_queue = Queue("Macrotask Queue")
microtask_queue = Queue("Microtask Queue")



def push_stack(fn):
    call_stack.append(fn.__name__)
    print(f"CALL STACK PUSH: {fn.__name__}")

def pop_stack():
    fn = call_stack.pop()
    print(f"CALL STACK POP: {fn}")



def set_timeout(fn):
    """Simulates setTimeout / IO / DOM events"""
    macrotask_queue.enqueue(fn)

def queue_microtask(fn):
    """Simulates Promise.then / queueMicrotask"""
    microtask_queue.enqueue(fn)



def event_loop_step():
    """
    One iteration of the JS event loop
    """

    if not macrotask_queue.is_empty():
        task = macrotask_queue.dequeue()
        push_stack(task)
        task()
        pop_stack()

    while not microtask_queue.is_empty():
        micro = microtask_queue.dequeue()
        push_stack(micro)
        micro()
        pop_stack()



def main_script():
    print("Main script start")

    set_timeout(timer_task)
    queue_microtask(promise_task_1)

    print("Main script end")


def timer_task():
    print("Timer task running")


def promise_task_1():
    print("Promise task 1 running")

    queue_microtask(promise_task_2)


def promise_task_2():
    print("Promise task 2 running")



print("\n--- JS ENGINE SIMULATION START ---\n")

macrotask_queue.enqueue(main_script)

for _ in range(5):
    event_loop_step()
    time.sleep(0.5)
