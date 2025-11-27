"""
Модуль для вычисления чисел Фибоначчи и факториала.
Реализованы итеративная и рекурсивная версии функций.
"""
#фибоначчи
def fibo(n: int) -> int:
    """
        Вычисляет n-ое число Фибоначчи итеративным методом.
        Args:
            n (int): Номер числа Фибоначчи (должен быть неотрицательным)
        Returns:
            int: n-ое число Фибоначчи
        Raises:
            ValueError: Если n < 0
        """
    if n < 0:
        raise ValueError('n must be positive')
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

#фибоначчи рекурсивно
def fibo_recursive(n):
    """
        Вычисляет n-ое число Фибоначчи рекурсивным методом.
        Args:
            n (int): Номер числа Фибоначчи (должен быть неотрицательным)
        Returns:
            int: n-ое число Фибоначчи
        Raises:
            ValueError: Если n < 0
        """
    if n < 0:
        raise ValueError('n must be positive')
    if n <= 1:
        return n
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)


#факториал
def factorial(n: int) -> int:
    """
        Вычисляет факториал числа n итеративным методом.
        Args:
            n (int): Число для вычисления факториала (должно быть неотрицательным)
        Returns:
            int: Факториал числа n
        Raises:
            ValueError: Если n < 0
        """
    if n<0:
        raise ValueError('Negative numbers are not allowed')
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

#факториал рекурсивно
def factorial_recursive(n: int) -> int:
    """
        Вычисляет факториал числа n рекурсивным методом.
        Args:
            n (int): Число для вычисления факториала (должно быть неотрицательным)
        Returns:
            int: Факториал числа n
        Raises:
            ValueError: Если n < 0
        """
    if n<0:
        raise ValueError('Negative numbers are not allowed')
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
