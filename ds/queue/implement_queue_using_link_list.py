'''
in queue data structure there are two main pointers front and rear
the front points to the first item and rear points to the last item
en_queue() this operation adds a new node after rear and moves rear to next node
de_queue() this operation removes the front node and moves front to next
'''


class Node(object):

    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node


class LinkedList(object):

    def __init__(self):
        self._head = None

    def __iter__(self):
        current = self._head
        while current:
            yield current.get_data()
            current = current.get_next()

    def insert_front(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            return self._head
        current = self._head
        while current and current.get_next() is not None:
            current = current.get_next()

        current.set_next(new_node)
        return self._head

    def insert_after(self, data, node):
        new_node = Node(data)
        if node is not None:
            node_next = node.get_next()
            node.set_next(new_node)
            new_node.set_next(node_next)


    def insert_end(self, data):
        new_node = Node(data)
        current = self._head
        if current is None:
            self._head = new_node
            return
        while current and current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def get_head(self):
        return self._head

    def get_tail(self):
        current = self._head
        while current and current.get_next():
            current = current.get_next()
        return current

    def delete_head(self):
        elem = self._head
        if elem is None:
            print 'Cannot delete as it is empty'
            return
        self._head = elem.get_next()
        print 'Deleting', elem.get_data()
        del elem


class Queue(object):

    def __init__(self):
        self._front = None
        self._rear = None
        self._linked_list = LinkedList()

    def get_front(self):
        return self._front

    def get_rear(self):
        return self._rear

    def en_queue(self, elem):
        print 'Enqueuing', elem
        if self._front is None and self._rear is None:
            self._linked_list.insert_end(elem)
            self._front = self._linked_list.get_head()
            self._rear = self._linked_list.get_head()
            return
        self._linked_list.insert_end(elem)
        self._rear = self._rear.get_next()


    def de_queue(self):
        self._linked_list.delete_head()
        self._front = self._linked_list.get_head()

    def is_empty(self):
        if self._front is None and self._rear is None:
            return True
        return False


def main():
    queue_obj = Queue()
    queue_obj.en_queue(1)
    queue_obj.en_queue(2)
    queue_obj.en_queue(3)
    queue_obj.en_queue(4)
    queue_obj.en_queue(5)
    queue_obj.de_queue()
    queue_obj.de_queue()

if __name__ == '__main__':
    main()
