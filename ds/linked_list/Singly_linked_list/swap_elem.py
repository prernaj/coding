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

    def swap_elem(self, key1, key2):
        print 'Swapping', key1, key2
        first_node = second_node = prev_first_node = prev_second_node = None
        if self._head.get_data() == key1:
            first_node = self._head
        if self._head.get_data() == key2:
            second_node = self._head
        current = self._head
        while current:
            if first_node and second_node:
                break
            next_elem = current.get_next()
            if next_elem:
                if next_elem.get_data() == key1:
                    prev_first_node = current
                    first_node = next_elem
                if next_elem.get_data() == key2:
                    prev_second_node = current
                    second_node = next_elem
            current = current.get_next()
        if first_node is None or second_node is None:
            print 'Cannot swap'
            return
        if prev_first_node:
            prev_first_node.set_next(second_node)
        if prev_second_node:
            prev_second_node.set_next(first_node)
        temp = first_node.get_next()
        first_node.set_next(second_node.get_next())
        second_node.set_next(temp)
        if self._head.get_data() == key1:
            self._head = second_node
        elif self._head.get_data() == key2:
            self._head = first_node

def main():
    link_list_obj = LinkedList()
    link_list_obj.insert_front(1)
    link_list_obj.insert_front(2)
    head_node = link_list_obj.get_head()
    if head_node:
        link_list_obj.insert_after(3, head_node.get_next())
    link_list_obj.insert_end(4)
    for item in link_list_obj:
        print item,
    link_list_obj.swap_elem(3,2)
    for item in link_list_obj:
        print item,

if __name__=='__main__':
    main()
