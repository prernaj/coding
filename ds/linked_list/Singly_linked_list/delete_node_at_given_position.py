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
    link_list_obj = LinkedList()
    link_list_obj.insert_front(1)
    link_list_obj.insert_front(2)
    h = link_list_obj.get_head()
    if h:
        link_list_obj.insert_after(3, h.get_next())
    link_list_obj.insert_end(4)
    link_list_obj.delete_key(3)
    link_list_obj.delete_at_position(0)
    link_list_obj.delete_at_position(1)
    for item in link_list_obj:
        print item,

if __name__=='__main__':
    main()





