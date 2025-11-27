#реализация структур данных
# 1.Стек
# b.Стек на list

class Stack:
    """
        Реализация стека (LIFO - Last In, First Out) на основе списка.
    """

    def __init__(self):
        self.items = []
    def push(self, item: int):
        #добавление элемента 'наверх'
        self.items.append(item)
    def pop(self):
        #удвление элемента с 'верхушки'
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.items.pop()
    def peek(self):
        #просмотр 'верхнего' элемента без удаления
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.items[-1]
    def is_empty(self):
        return self.items == []
    def __len__(self):
        return len(self.items)

# 2. Очередь
# b. Очередь на list
class Queue:
    """
        Реализация очереди (FIFO - First In, First Out) на основе списка.
    """
    def __init__(self):
        self.items = []
    def enqueue(self, item: int):
        self.items.append(item) #добавление элемента в очередь
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.items.pop(0) #удаление элемента из очереди или вызывает исключение при пустой очереди
    def is_empty(self):
        return self.items == []
    def __len__(self):
        return len(self.items)
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.items[0]
