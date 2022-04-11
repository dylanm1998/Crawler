import threading

value = 0

def add_value():
    # If a global variable is modified in a function, it needs to be declared using the global keyword
    global value
    for x in range(100):
        value += 1
    print("The value of value is %d"%value)

def main():
    for x in range(2):
        th = threading.Thread(target=add_value())
        th.start()

if __name__ == '__main__':
    main()