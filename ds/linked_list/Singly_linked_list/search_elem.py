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

    def __iter__(self):
        current = self._head
        while current:
            yield current.get_data()
            current = current.get_next()

    def insert_front(self, data):
        new_node = Node(data)
        if self._head == None:
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
        while current and current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def get_head(self):
        return self._head

    def search_elem(self, key):
        current = self._head
        while current:
            if current.get_data() == key:
                return current
            current = current.get_next()
        return None

    

def main():
    link_list_obj = LinkedList()
    link_list_obj.insert_front(1)
    link_list_obj.insert_front(2)
    h = link_list_obj.get_head()
    if h:
        link_list_obj.insert_after(3, h.get_next())
    link_list_obj.insert_end(4)
    for item in link_list_obj:
        print item,
    s_node = link_list_obj.search_elem(2)
    print 'Node at ', s_node.get_data()

if __name__=='__main__':
    main()
