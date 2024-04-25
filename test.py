import threading
import queue

def consumer(q):
    while True:
        item = q.get()
        print('Consume:', item)
        
        q.task_done() 
        
def producer(q):
    for i in range(10):
        q.put(i)

q = queue.Queue()

consumer_thread1 = threading.Thread(target=consumer, args=(q,))
consumer_thread2 = threading.Thread(target=consumer, args=(q,))


consumer_thread1.start()
consumer_thread2.start()
producer(q)
q.join()



"""
使用list的pop效率是O(n)，而使用queue.get()效率是O(1)
queue是线程安全的，get是一个阻塞操作。如果使用list，需要上锁
"""
