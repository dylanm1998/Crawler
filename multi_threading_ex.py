import time
import threading

# def coding():
#     the_tread = threading.current_thread()
#     print(the_tread.name)
#     for x in range(3):
#         print("%s is coding..."% the_tread.name)
#         time.sleep(1)
#
# def drawing():
#     the_tread = threading.current_thread()
#     for x in range(3):
#         print("%s is drawing..."% the_tread.name)
#         time.sleep(1)
#
# def multi_thread():
#     th1 = threading.Thread(target=coding,name='Tom')
#     th2 = threading.Thread(target=drawing,name='Amy')
#
#     th1.start()
#     th2.start()
#
#     print(threading.enumerate())
#
# if __name__ == '__main__':
#     multi_thread()

# =======================================================

class CodingThread(threading.Thread):
    def run(self) -> None:
        the_thread = threading.current_thread()
        for x in range(3):
            print("%s is coding" % the_thread.name)
            time.sleep(1)

class DrawingThread(threading.Thread):
    def run(self) -> None:
        the_thread = threading.current_thread()
        for x in range(3):
            print("%s is drawing" % the_thread.name)
            time.sleep(1)

def multi_thread():
    th1 = CodingThread()
    th2 = DrawingThread()

    th1.start()
    th2.start()

if __name__ == '__main__':
    multi_thread()