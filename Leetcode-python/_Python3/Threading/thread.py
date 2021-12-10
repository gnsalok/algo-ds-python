import threading

def printCube(num):
    print("Cube: {}\n".format(num*num*num))

def printSquare(num):
    print("Square: {}\n".format(num * num))

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=printSquare, args=(10,))
    t2 = threading.Thread(target=printCube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

     # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")











