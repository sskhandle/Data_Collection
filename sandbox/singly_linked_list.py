class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def display(self):
        node_list = []
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            node_list.append(cur_node.data)
        print (node_list)

    def length(self):
        count = 0
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            count += 1
        return count

    def search(self, elem):
        cur_node = self.head
        idx = 0
        while cur_node.next:
            cur_node = cur_node.next
            if cur_node.data == elem:
                return 'The element {} is at index {}'.format(elem, idx)
            idx += 1
        return "Element not found in linked list"

    def delete(self, elem):
        cur_node = self.head
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == elem:
                if cur_node.next:
                    prev_node.next = cur_node.next
                else:
                    prev_node.next = None


if __name__ == '__main__':

    ll = LinkedList()
    ll.append(3)
    ll.append(6)
    ll.append(2)
    ll.append(5)

    ll.display()

    print (ll.length())

    print (ll.search(4))

    ll.delete(3)

    ll.display()