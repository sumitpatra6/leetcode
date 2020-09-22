class MyQueue(object):

    def __init__(self, size):
        super().__init__()
        self.size = size
        self.data = [None]*self.size
        self.start_pointer = 0
        self.end_pointer = 0

    def enqueue(self, value):
        """
        Return true if enqueue is succesfull else return false
        """
        if self.end_pointer == self.size :
            return False
        self.data[self.end_pointer] = value
        self.end_pointer += 1
        return True

    def dequeue(self):
        """
        delete an element from the queue, return true if the operation is successfull
        else return false
        """
        if self.is_empty():
            return False
        else:
            self.data[self.start_pointer] = None
            self.start_pointer += 1
            if self.start_pointer == self.size:
                self.start_pointer = 0
                self.end_pointer = 0

    def front(self):
        """
        Get the front item of the queue
        """
        if self.is_empty():
            return None
        return self.data[self.end_pointer - 1]

    def is_empty(self):
        """
        Check whether the queue is empty or not
        """
        if self.start_pointer == 0 and self.end_pointer ==0:
            return True
        return False
    
    def print_queue(self):
        print(self.data)


class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.data = [None]*k
        self.front = -1
        self.rear = -1
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        # checking for empty queue
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.data[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.rear == self.front:
            # only one value in the queue
            self.data[self.rear] = None
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        # print(self.front, self.rear)
        if self.isEmpty():
            # print('...')
            return None
        else:
            print('.,.')
            return self.data[self.front]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return None
        return self.data[self.rear]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.front == -1:
            return True
        return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if (self.rear + 1) % self.size == self.front:
            return True
        return False
        

circular_queue = MyCircularQueue(6)
print(circular_queue.enQueue(6))
print(circular_queue.Rear())
print(circular_queue.Rear())
print(circular_queue.deQueue())
print(circular_queue.enQueue(5))
print(circular_queue.Rear())
print(circular_queue.deQueue())
print(circular_queue.Front())
print(circular_queue.deQueue())
print(circular_queue.deQueue())
print(circular_queue.deQueue())