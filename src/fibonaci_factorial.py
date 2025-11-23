#фибоначчи
def fibo(n: int) -> int:
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
    if n < 0:
        raise ValueError('n must be positive')
    if n <= 1:
        return n
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)


#факториал
def factorial(n: int) -> int:
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
    if n<0:
        raise ValueError('Negative numbers are not allowed')
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
