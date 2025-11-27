import unittest
from src.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)

    def test_stack_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.stack.peek()
