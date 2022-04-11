import threading
import random
import time

gMoney = 0
gCondition = threading.Condition()
gTimes = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            gCondition.acquire()
            if gTimes >= 10:
                gCondition.release()
                break
            money = random.randint(0, 100)
            gMoney += money
            gTimes += 1
            print("%s made %d dollars and left %d dollars"%(threading.current_thread().name,money,gMoney))
            gCondition.notify_all()
            gCondition.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        while True:
            gCondition.acquire()
            money = random.randint(0,100)
            while gMoney < money:
                if gTimes >= 10:
                    print("%s wants to spend %d dollars, but the balance is only %d dollars, and the producer is no longer making!"%(threading.current_thread().name,money,gMoney))
                    gCondition.release()
                    return
                print("%s wants to spend %d yuan, but the balance is only %d dollars, the consumption fails!"%(threading.current_thread().name,money,gMoney))
                gCondition.wait()
            gMoney -= money
            print("%s spent %d dollars, leaving %d dollars"%(threading.current_thread().name,money,gMoney))
            gCondition.release()
            time.sleep(1)


def main():
    for x in range(5):
        th = Producer(name="Producer %d"%x)
        th.start()

    for x in range(5):
        th = Consumer(name="Consumer %d"%x)
        th.start()

if __name__ == '__main__':
    main()