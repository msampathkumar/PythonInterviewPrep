class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


def _prepare_random_data():
    ll = LinkedList()
    for each in [12, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6]:
        ll.add(each)
    return ll


def first_question(linkedlist):
    """Write code to remove duplicates from an unsorted linked list FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed"""
    pointer = linkedlist.head
    while pointer and pointer.next:
        # print(pointer.value)
        second_pointer = pointer
        data = second_pointer.value
        # print('--' * 5)
        while second_pointer and second_pointer.next:
            # print(data, second_pointer.next.value)
            if data == second_pointer.next.value:
                # double jump
                second_pointer.next = second_pointer.next.next
            else:
                # single jump
                second_pointer = second_pointer.next
        pointer = pointer.next


def second_question(linkedlist, n):
    """Implement an algorithm to find the nth to last element of a singly linked list"""
    first_pointer = linkedlist.head
    second_pointer = linkedlist.head
    for i in range(n):
        print(f'skipping ({second_pointer.value} -> {second_pointer.next.value})')
        second_pointer = second_pointer.next

    while second_pointer.next:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    print(first_pointer.value, second_pointer.value)

if __name__ == '__main__':
    ll = _prepare_random_data()
    # print('---1' * 5)
    # ll.print()
    print('---2' * 5)
    first_question(ll)
    second_question(ll, 2)
    print('---3' * 5)
    ll.print()
