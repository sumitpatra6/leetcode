import random
import threading
from concurrent.futures import ThreadPoolExecutor
SENTINEL = object()

class PipeLine:
    def __init__(self):
        self.message = 0
        self.consumer_lock = threading.Lock()
        self.producer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        print("{}: About to acquire getlock".format(name))
        self.consumer_lock.acquire()
        print("{}: Got get lock".format(name))
        message = self.message
        print("{}: About to release set lock".format(name))
        self.producer_lock.release()
        print("{}: Released set lock".format(name))
        return message

    def set_message(self, message, name):
        print("{}, about to acquire set lock".format(name))
        self.producer_lock.acquire()
        print("{}: got set lock".format(name))
        self.message = message
        print("{}: About to release get lock".format(name))
        self.consumer_lock.release()
        print("{}: Released get lock".format(name))


def producer(pipeline):
    for index in range(10):
        message = random.randint(1, 101)
        print("Producer got message {}".format(message))
        pipeline.set_message(message, 'Producer')
    pipeline.set_message(SENTINEL, 'Producer')


def consumer(pipeline):
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message('Consumer')
        if message is not SENTINEL:
            print("Consumer storing message {}".format(message))


if __name__ == '__main__':
    pipeline = PipeLine()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)