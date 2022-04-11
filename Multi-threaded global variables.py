import threading

value = 0

gLock = threading.Lock()


def add_value():
    # If the global variable is modified in the function, then you need to use
    # global keyword to declare
    global value
    gLock.acquire()
    for x in range(1000000):
        value += 1
    gLock.release()
    print("valuen is：%d"%value)

def main():
    for x in range(2):
        th = threading.Thread(target=add_value)
        th.start()

if __name__ == '__main__':
    main()