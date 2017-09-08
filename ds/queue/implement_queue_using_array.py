class MyQueue():
    
    def __init__(self, max_size):
        self._queue = []
        self._size = -1
        self._max_size = max_size

    def enqueue(self, elem):
        if self._size == self._max_size:
            print 'Queue is full'
        else:
            self._size += 1
            self._queue.insert(self._size, elem)
    
    def dequeue(self):
        if self._size == -1:
            print 'Queue is empty'
        else:
            ret = self._queue[self._size]
            self._size -= 1
            return ret
    
    def get_size(self):
        return self._size

    def get_front(self):
        return self._queue[0]

    def get_rear(self):
        return self._queue[self._size]

def main():
    max_size = 10
    q = MyQueue(10)
    q.enqueue(1)
    q.enqueue(2)
    print q.dequeue()

if __name__=='__main__':
    main()
