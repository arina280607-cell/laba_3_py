"""
Модуль с реализацией алгоритмов сортировки.
Включает пузырьковую, быструю, подсчетом, поразрядную, блочную сортировки и сортировку кучей.
"""
#пузырьковая сортировка
def bubble_sort(a: list[int]) -> list[int]:
    """
    Сортировка пузырьком.

    Args:
        a (list[int]): Исходный список для сортировки

    Returns:
        list[int]: Отсортированный список
    """
    n = len(a)
    for i in range(n):
        # Проходим по массиву, сравнивая соседние элементы
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                # Меняем местами, если текущий элемент больше следующего
                a[j], a[j+1] = a[j+1], a[j]
    return a


#быстрая сортировка
def quick_sort(a: list[int]) -> list[int]:
    """
        Быстрая сортировка.
        Args:
            a (list[int]): Исходный список для сортировки
        Returns:
            list[int]: Отсортированный список
        """
    n = len(a)
    if n <= 1:
        return a
    # Выбираем опорный элемент
    pivot = a[n//2]
    # Разделяем на три списка: меньше, равно и больше опорного
    men = []
    ravn = []
    bol = []
    for i in a:
        if i < pivot:
            men.append(i)
        elif i > pivot:
            bol.append(i)
        else:
            ravn.append(i)
    # Рекурсивно сортируем подсписки и объединяем
    return quick_sort(men) + ravn + quick_sort(bol)


#count sort
def counting_sort(a: list[int]) -> list[int] :
    """
        Сортировка подсчетом.
        Args:
            a (list[int]): Исходный список для сортировки
        Returns:
            list[int]: Отсортированный список
        """
    if not a:
        return []
    # Находим минимальное и максимальное значения
    ma= max(a)
    mi= min(a)
    count = [0] * (ma - mi + 1)
    sp=[0] * len(a)
    # Подсчитываем количество каждого элемента
    for i in range(len(a)):
        count[a[i]-mi] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    for i in range (len(a) - 1, -1, -1):
        sp[count[a[i]-mi] - 1] = a[i]
        count[a[i]-mi] -= 1
    return sp


#radix sort
def radix_sort(a: list[int]) -> list[int]:
    """
        Поразрядная сортировка.

        Args:
            a (list[int]): Исходный список для сортировки
        Returns:
            list[int]: Отсортированный список
        Raises:
            ValueError: Если в массиве есть отрицательные числа
        """
    if not a:
        return []
    if min(a) < 0:
        raise ValueError("radix sort can only be applied to positive integers")
    ma = max(a)
    exp = 1
    while ma//exp > 0:
        counting_s(a, exp)
        exp = exp * 10
    return a

def counting_s(a: list[int], exp: int) -> None:
    """
       Вспомогательная функция для поразрядной сортировки.
       Выполняет устойчивую сортировку по текущему разряду.
    """
    n = len(a)
    output = [0] * n
    count = [0] * 10
    # Подсчитываем количество каждого цифрового значения
    for i in range(n):
        digit = (a[i] // exp) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        digit = a[i] // exp % 10
        output[count[digit] - 1] = a[i]
        count[digit] -= 1
    for i in range(n):
        a[i] = output[i]


#bucket sort (для float в диапазоне [0, 1))
def insertion_sort(s: list[float]):
    for i in range(1, len(s)):
        k = s[i]
        j = i - 1
        while j >= 0 and k < s[j]:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = k

def bucket_sort(a: list[float]):
    """
        Блочная сортировка для чисел в диапазоне [0, 1).
        Args:
            a (list[float]): Исходный список для сортировки
        Returns:
            list[float]: Отсортированный список
        """
    if not a:
        return []
    n = len(a)
    buckets = [[] for _ in range(n)]
    # Распределяем элементы по блокам
    for x in a:
        b = int(x * n)
        buckets[b].append(x)
    for bucket in buckets:
        insertion_sort(bucket)
    index = 0
    for bucket in buckets:
        for x in bucket:
            a[index] = x
            index += 1
    return a

#heap sort
def heap_sort(a):
    """
        Сортировка кучей (Heap Sort).
        Args:
            a (list[int]): Исходный список для сортировки
        Returns:
            list[int]: Отсортированный список
        """
    n = len(a)
    def build_max_heap(sp):
        for i in range(n//2 - 1, -1, -1):
            heapify(sp, n, i)
    def heapify(sp, ln, i):
        # функция для обмена элементов в куче, чтобы на вершине был самый большой
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        # Находим наибольший элемент среди родителя и его потомков
        if left < ln and sp[left] > sp[largest]:
            largest = left
        if right < ln and sp[right] > sp[largest]:
            largest = right
        if largest != i:
            sp[i], sp[largest] = sp[largest], sp[i]
            heapify(sp, ln, largest)
    build_max_heap(a)
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
    return a









