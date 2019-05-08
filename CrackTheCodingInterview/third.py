class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    "Last In, Last Out"

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        if self.data:
            return True
        else:
            return False


class Queue:
    """First in, Last Out"""

    def __init__(self):
        self.head = None

    def queue(self, value):
        if self.head is None:
            self.head = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def dequeue(self):
        if self.head:
            data = self.head.value
            self.head = self.head.next
            return data
        else:
            return 0


class StacksSet:
    """Imagine a (literal) stack of plates If the stack gets too high, it might topple There- fore, in real life, we would likely start a new stack when the previous stack exceeds some threshold Implement a data structure SetOfStacks that mimics this SetOf- Stacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity SetOfStacks push() and SetOfStacks pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack)
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack"""

    def __init__(self):
        self.master_stack = Stack()
        self.stack_limit = 5
        self.current_stack_limit = None
        self.current_stack = None

    def push(self, value):

        if self.current_stack is None:
            self.current_stack = Stack()
            self.current_stack_limit = 0

        if self.current_stack_limit >= self.stack_limit:
            self.master_stack.push(self.current_stack)
            self.current_stack = Stack()
            self.current_stack_limit = 0

        if self.current_stack_limit < self.stack_limit:
            self.current_stack.push(value)
            self.current_stack_limit += 1

    def pop(self):
        if self.current_stack_limit < 1:
            if self.master_stack:
                # get new stack
                self.current_stack = self.master_stack.pop()
                self.current_stack_limit = self.stack_limit
            else:
                return 0
        self.current_stack_limit -= 1
        return self.current_stack.pop()


def _StackTesting():
    SS = StacksSet()
    for i in range(100):
        SS.push(i)
    for i in range(100):
        print(SS.pop())




def HanoiTower(N):
    def moveTower(height, aPole, bPole, cPole):
        if height >= 1:
            data = [height, aPole, bPole, cPole]
            print(data)
            moveTower(height - 1, aPole, cPole, bPole)
            moveDisk(aPole, bPole, height - 1)
            moveTower(height - 1, cPole, bPole, aPole)
    def moveDisk(fp, tp, ht):
        print("moving disk from", fp, "to", tp, "of height", ht)
    moveTower(N, "A", "B", "C")


def SortStack():
    aStack = Stack()
    for i in [4, 2, 1, 5, 6]:
        aStack.push(i)
    bStack = Stack()
    print(aStack.data)
    print(bStack.data)
    while (not aStack.data):
        tmp = aStack.pop()
        print(tmp)
        while((not bStack.data) and (tmp > bStack.data[-1])):
            aStack.push(bStack.pop())
        bStack.push(tmp)
    print(aStack.data)
    print(bStack.data)

if __name__ == '__main__':
    # HanoiTower(2)
    SortStack()




