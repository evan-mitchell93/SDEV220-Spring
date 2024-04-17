import random

def my_num():
    return random.random()

def my_int():
    return random.randint(0,10)


if __name__ == "__main__":
    #bad breaking of tests :(
    print(type(my_num()))
    print(int(my_num()))