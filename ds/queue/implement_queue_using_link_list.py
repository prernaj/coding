'''
in queue data structure there are two main pointers front and rear
the front points to the first item and rear points to the last item
enQueue() this operation adds a new node after rear and moves rear to next node
deQueue() this operation removes the front node and moves front to next
'''


class Node():
    
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node


class LinkedList():

    def __init__(self):
        self._head = None

    def insert_front(self, data):
        new_node = Node(data)
        if self._head == None:
            self._head = new_node
            return self._head
        temp = self._head
        while temp and temp.get_next() is not None:
            temp = temp.get_next()

        temp.set_next(new_node)
        return self._head

    def insert_after(self, data, node):
        new_node = Node(data)
        if node is not None:
            node_next = node.get_next()
            node.set_next(new_node)
            new_node.set_next(node_next)


    def insert_end(self, data):
        new_node = Node(data)
        temp = self._head
        if temp == None:
            self._head = new_node
            return
        while temp and temp.get_next() is not None:
            temp = temp.get_next()
        temp.set_next(new_node)

    def get_head(self):
        return self._head

    def get_tail(self):
        temp = self._head
        while temp and temp.get_next():
            temp = temp.get_next()
        return temp

    def print_ll(self):
        temp = self._head
        while temp:
            print temp.get_data(),
            temp = temp.get_next()

    def delete_head(self):
        elem = self._head
        if elem == None:
            print 'Cannot delete as it is empty'
            return
        self._head = elem.get_next()
        print 'Deleting', elem.get_data()
        del elem
    

class Queue():

    def __init__(self):
        self._front = None
        self._rear = None
        self._linked_list = LinkedList()

    def get_front(self):
        return self._front

    def get_rear(self):
        return self._rear

    def enQueue(self, elem):
        print 'Enqueuing', elem
        if self._front == None and self._rear == None:
            self._linked_list.insert_end(elem)
            self._front = self._linked_list.get_head()
            self._rear = self._linked_list.get_head()
            return
        self._linked_list.insert_end(elem)
        self._rear = self._rear.get_next()


    def deQueue(self):
        self._linked_list.delete_head()
        self._front = self._linked_list.get_head()

    def isEmpty(self):
        if self_front == None and self._rear == None:
            return True
        return False

    def print_queue(self):
        self._linked_list.print_ll()


def main():
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.enQueue(4)
    q.enQueue(5)
    q.print_queue()
    q.deQueue()
    q.deQueue()
    q.print_queue()

if __name__=='__main__':
    main()





