import unittest
from src.fibonaci_factorial import fibo, factorial_recursive, fibo_recursive, factorial
class TestFibonacciFactorial(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(fibo(0), 0)
        self.assertEqual(fibo(1), 1)
        self.assertEqual(fibo(2), 1)
        self.assertEqual(fibo(3), 2)
        self.assertEqual(fibo(4), 3)
        self.assertEqual(fibo(5), 5)
        self.assertEqual(fibo(6), 8)
        self.assertEqual(fibo(10), 55)
    def test_fibo_recursive(self):
        self.assertEqual(fibo_recursive(0), 0)
        self.assertEqual(fibo_recursive(1), 1)
        self.assertEqual(fibo_recursive(2), 1)
        self.assertEqual(fibo_recursive(3), 2)
        self.assertEqual(fibo_recursive(4), 3)
        self.assertEqual(fibo_recursive(10), 55)

    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(1), 1)
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(7), 5040)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

    def negative_tests(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial_recursive(-1)
        with self.assertRaises(ValueError):
            fibo_recursive(-1)
        with self.assertRaises(ValueError):
            fibo(-1)
