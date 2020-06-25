class LinkedList(object):
    """
    This is an implementation of a LinkedList in python.
    """

    def __init__(self):
        self.head = None

    def print_ll(self, node=None):
        if not node:
            node = self.head

        print(node.value)

        # Calling the print_ll recursively
        if node.next:
            self.print_ll(node.next)
        else:
            print('End of LinkedList')

    def reverse(self):
        """
        Consider a linked list of the below shape and size.
        Value:                | Head |     | 10 |   | 3 |   | 4 |  | 1 |
                              -------      -----    ----    ----   ----
        Addresses:            | 121 |      |234|    |34|    |12|  |None|

        We want to change this to;
        Value:                | Head |     | 1 |   | 4 |   | 3 |  | 10 |
                              -------      ----    ----    ----   -----
        Addresses:            | 12  |      |34|   |234|   |121|  |None|

        :return: None
        """

        if self.head:
            prev_address = None
            node = self.head

            while node:

                proxy_node = node
                node = node.next

                proxy_node.next = prev_address

                prev_address = proxy_node

            self.head = prev_address


class Node(object):
    """
    A Node in a LinkedList that points to another node and has a value
    """

    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)

    b.next = c
    a.next = b

    ll = LinkedList()
    ll.head = a

    ll.reverse()
    ll.print_ll()