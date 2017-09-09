'''
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
        while temp and temp.get_next() is not None:
            temp = temp.get_next()
        temp.set_next(new_node)

    def get_head(self):
        return self._head

    def print_ll(self):
        temp = self._head
        while temp:
            print temp.get_data(),
            temp = temp.get_next()

    def delete_key(self, item):
        temp = self._head
        while temp:
            if temp.get_next() == None:
                print 'Cannot find key'
                return
            if temp.get_next().get_data() == item:
                elem = temp.get_next()
                temp.set_next(elem.get_next())
                print 'Deleting', elem.get_data()
                del elem
                return
            temp = temp.get_next()

    def delete_at_position(self, pos):
        ind = 0
        temp = self._head
        if pos == 0:
            self._head = temp.get_next()
            print 'Deleting', temp.get_data()
            del temp
            return
        while temp:
            if ind == pos-1:
                elem = temp.get_next()
                temp.set_next(elem.get_next())
                print 'Deleting', elem.get_data()
                del elem
                return

    

def main():
    ll = LinkedList()
    ll.insert_front(1)
    ll.insert_front(2)
    h = ll.get_head()
    if h:
        ll.insert_after(3, h.get_next())
    ll.insert_end(4)
    ll.print_ll()
    ll.delete_key(3)
    ll.print_ll()
    ll.delete_at_position(0)
    ll.print_ll()
    ll.delete_at_position(1)
    ll.print_ll()

if __name__=='__main__':
    main()





