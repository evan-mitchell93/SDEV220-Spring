from multiprocessing import Process
import time


def f1(*args):
    print(f"We are doing something {args}")
    time.sleep(7)
    print("We are now doing something later")

def f2():
    print("No sleep until the end")
    print("Resist the sleep")
    time.sleep(10)

if __name__ == "__main__":
    process1 = Process(target=f1, args=("Evan", "Bob"))
    process2 = Process(target=f2)

    process1.start()
    process2.start()

    #don't do anything until these finish
    process1.join()
    process2.join()

    print("End of main")