"""
Jack Sanders
CIS 314
Lab1 Test Cases
10/25/2019

Unit Test Cases
"""


import lab1
import unittest


class T0_TestingQueue(unittest.TestCase):
    
    def test_basic_enqueue(self):
        #testing the basic enqueue operation
        print("\n")
        print("Testing Queue : Enqueue")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.printQueue(), [1,2,3,4])
        print("\n")

    def test_enqueue_dequeue(self):
        #testing the basic enqueue operation
        print("\n")
        print("Testing Queue : Enqueue and Dequeue")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.dequeue()
        q.enqueue(3)
        q.enqueue(4)
        q.dequeue()
        self.assertEqual(q.printQueue(), [3,4])
        print("\n")

    def test_dequeue(self):
        #testing the basic enqueue operation
        print("\n")
        print("Testing Queue : Returning Empty Queue")
        q = lab1.Queue()
        q.enqueue(1)
        q.dequeue()
        self.assertEqual(q.printQueue(), [])
        print("\n")

    def test_is_empty_false(self):
        #testing if queue is empty
        print("\n")
        s = lab1.Queue()
        s.enqueue("4")
        print("return false if the queue is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")


class T1_TestingStack(unittest.TestCase):

    def test_basic_push(self):
        #testing the basic enqueue operation
        print("\n")
        print("Testing Stack : Push")
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        self.assertEqual(s.printStack(), [4,3,2,1])
        print("\n")

    def test_push_pop(self):
        #testing stack push operation
        print("\n")
        print ("Testing Stack: Push and Pop")
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.pop()
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(s.printStack(), [5,4,3,1])
        print("\n")

    def test_pop(self):
        #testing stack push operation
        print("\n")
        print ("Testing Stack: Returning Empty Stack")
        s = lab1.Stack()
        s.pop()
        self.assertEqual(s.printStack(), [])
        print("\n")

    def test_is_empty_false(self):
        #testing if stack is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")


class T2_TestingPalindrome(unittest.TestCase):
    
    def test_basic_string_false(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

    def test_basic_string_true(self):
        # testing with basic string
        print("\n")
        string = "hannah"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")

    def test_complex_string_false(self):
        # testing with basic string
        print("\n")
        string = "{(< .AAba. >)}"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

    def test_complex_string_true(self):
        # testing with basic string
        print("\n")
        string = "{ < : [ 12345 abCdDcBA 54321 [ : < {"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")

if __name__ == '__main__':
    unittest.main()
