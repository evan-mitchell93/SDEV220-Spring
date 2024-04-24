from multiprocessing import Process, Queue
import time

def p1(q):
    while True:
        q.put("Hello")
        time.sleep(2)

def p2(q):
    while True:
        print(q.get())
        time.sleep(4)

if __name__=="__main__":
    q = Queue()

    process1 = Process(target=p1, args=(q,))
    process2 = Process(target=p2,args=(q,))

    process1.start()
    process2.start()

    process2.join()
    process1.join()

