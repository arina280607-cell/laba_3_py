"""
Модуль тестирования структур данных: стека и очереди.
"""

import unittest
from src.stack import Stack
from src.stack import Queue

class TestStack(unittest.TestCase):
    """Тесты для реализации стека."""
    #Инициализация стека перед каждым тестом
    def setUp(self):
        self.stack = Stack()
    #Тест добавления и удаления элементов из стека
    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
    #Тест просмотра верхнего элемента без удаления
    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)
    #Тест проверки пустоты стека
    def test_stack_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
    #Тесты исключения при удалении или просмотре из пустого стека
    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

class TestQueue(unittest.TestCase):
    """Тесты для реализации очереди."""
    def setUp(self):
        #Инициализация очереди перед каждым тестом.
        self.queue = Queue()

    def test_enqueue_dequeue(self) -> None:
        #Тест добавления и удаления элементов из очереди
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)

    def test_front(self) -> None:
        #Тест просмотра первого элемента без удаления.
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 2)

    def test_is_empty(self) -> None:
        #Тест проверки пустоты очереди.
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_dequeue_empty_queue(self) -> None:
        #Тест исключения при удалении из пустой очереди.
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_front_empty_queue(self) -> None:
        #Тест исключения при просмотре пустой очереди
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_length(self) -> None:
        #Тест определения размера очереди
        self.assertEqual(len(self.queue), 0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(len(self.queue), 2)
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 1)



if __name__ == "__main__":
    unittest.main()