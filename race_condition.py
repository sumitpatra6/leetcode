import time
from concurrent.futures import ThreadPoolExecutor
import threading


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        print("Thread {}, starting update".format(name))
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print("Thread {}, finishing update".fromat(name))

    def locked_update(self, name):
        print("Thread {}, starting update".format(name))
        print("Thread {}, about to lock".format(name))
        with self._lock:
            print("Thread {} has lock".format(name))
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print("Thread {}, about to release lock".format(name))
        print("Thread {}, released lock".format(name))
        print("Thread {}, finishing update".format(name))


if __name__ == '__main__':
    database = FakeDatabase()
    print("Testing update starting with value {}".format(database.value))
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update(index), index)
    print("Testing update, finishing with value {}".format(database.value))
