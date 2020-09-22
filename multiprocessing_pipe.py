import multiprocessing
import time
import os

def sender(conn, list):
    for l in list:
        conn.send(l)
        print("Sent message {} PID {}".format(l, os.getpid()))

def receiver(conn):
     while 1:
        msg = conn.recv()
        if msg == 'END':
            break
        print("Received message {}, PID {}".format(msg, os.getpid()))


if __name__ == '__main__':
    msgs = ["hello", "hey", "hru?", "END"]
    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()