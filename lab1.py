"""
Jack Sanders
CIS 313
Lab1
10/25/2019

queue, stack, and is-palindrome
"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.__data = data

        self.__next = next
            
    def setData(self, data):
        # Set the "data" data field to the corresponding input
        self.__data = data
    
    def setNext(self, next):
        # Set the "next" data field to the corresponding input
        self.__next = next

    def getData(self):
        # Return the "data" data field
        return self.__data

    def getNext(self):
        # return the "next" data field
        return self.__next


class Queue(object):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def enqueue(self, newData):
        # Create a new node whose data is newData and whose next node is null
        # Update head and tail
        # Hint: Think about what's different for the first node added to the Queue

        newQueueNode = Node(newData, None)
        if self.__tail is None:
            self.__tail = newQueueNode
            self.__head = newQueueNode
        else:
            self.__tail.setNext(newQueueNode)
            self.__tail = newQueueNode

    def dequeue(self):
        #  Return the head of the Queue
        #  Update head
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue

        if self.isEmpty():
            return None
        else:
            tempNode = self.__head
            self.__head = tempNode.getNext()
            if self.__head is None:
                self.__tail = None
            return tempNode.getData()

    def isEmpty(self):
        # Check if the Queue is empty

        return self.__head is None

    def printQueue(self):
        # Loop through your queue and print each Node's data

        queueList = []

        while self.__head is not None: # and self.__top.getNext() is not None:
            queueList.append(self.dequeue())
        return queueList


class Stack(object):
    def __init__(self):
        # We want to initialize our Stack to be empty
        # (ie) Set top as null
        self.__top = None
    
    def push(self, newData):
        # We want to create a node whose data is newData and next node is top
        # Push this new node onto the stack
        # Update top

        if self.isEmpty():
            self.__top = Node(newData, self.__top)
        else:
            newStackNode = Node(newData, self.__top)
            self.__top = newStackNode

    def pop(self):
        # Return the Node that currently represents the top of the stack
        # Update top
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack

        if self.isEmpty():
            return None
        else:
            topNode = self.__top
            self.__top = self.__top.getNext()
            return topNode.getData()

    def isEmpty(self):
        # Check if the Stack is empty

        return self.__top is None

    def printStack(self):
        # Loop through your stack and print each Node's data

        stackList = []
        while self.__top is not None: # and self.__top.getNext() is not None:
            stackList.append(self.pop())
        return stackList

#class TwoStackQueue(object):


def isPalindrome(s):
    # Use your Queue and Stack class to test whether an input is a palindrome
    myStack = Stack()
    myQueue = Queue()

    s = s.lower()
    s = s.split()
    new_s = ""

    for i in range(len(s)):
        new_s += s[i]

    length = len(new_s)
    pal_check = True
    for i in range(length):
        myStack.push(new_s[i])
        myQueue.enqueue(new_s[i])
    for i in range(length):
        if myStack.pop() != myQueue.dequeue():
            pal_check = False
    return pal_check