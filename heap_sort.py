class HeapSort:
    def __init__(self, array):
        self.array = array
        self.length = len(array)
        print(self.length)

    def heapify(self, i):
        left = 2*i+1
        right = 2*i + 2
        print(left, right)
        if left <= self.length- 1 and self.array[left] >= self.array[i]:
            largest = left
        else:
            largest = i
        print('----')
        if right <= self.length-1 and self.array[right] >= self.array[largest]:
            largest = right

        if largest != i:
            self.array[largest], self.array[i] = self.array[i], self.array[largest]
            self.heapify(largest)

    def build_max_heap(self):
        for i in range(int(self.length / 2) , 0, -1):
            print(i)
            self.heapify(i)

    def heap_sort(self):
        while self.length > 0:
            self.array[0], self.array[self.length - 1]  = self.array[self.length - 1], self.array[0]
            self.length -= 1
            self.heapify(0)



heap_sort = HeapSort([16,14,10,8,7,9,3,2,4,1])
heap_sort.build_max_heap()
heap_sort.heap_sort()
print(heap_sort.array)
