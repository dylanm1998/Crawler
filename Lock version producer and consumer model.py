import threading
import random

gMoney = 0
gLock = threading.Lock()
gTimes = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            gLock.acquire()
            if gTimes >= 10:
                gLock.release()
                break
            money = random.randint(0, 100)
            gMoney += money
            gTimes += 1
            print("%s made %d dollars"%(threading.current_thread().name,money))
            gLock.release()


class Consumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        while True:
            gLock.acquire()
            money = random.randint(0,100)
            if gMoney >= money:
                gMoney -= money
                print("%s spent %d dollars"%(threading.current_thread().name,money))
            else:
                if gTimes >= 10:
                    gLock.release()
                    break
                print("%s wants to spend %d dollars, but the balance is only %d"%(threading.current_thread().name,money,gMoney))
            gLock.release()


def main():
    for x in range(5):
        th = Producer(name="Producer %d"%x)
        th.start()

    for x in range(5):
        th = Consumer(name="Consumer %d number"%x)
        th.start()

if __name__ == '__main__':
    main()