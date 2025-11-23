#тут мы будем проверять насколько быстро работают сортировки в сравнении собычным sort()
import time
import random
from typing import List, Callable
from src.sorting import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort

# функция для тестирования скорости
def benchmark_sort(sort_func: Callable, data: List, name: str) -> float:
    start_time = time.perf_counter()
    sort_func(data.copy())
    end_time = time.perf_counter()
    return end_time - start_time

def compare_sorts():
    sizes = [100, 500, 1000]
    for size in sizes:
        #список случайных чисел для наших сортировок
        int_data = [random.randint(0, 1000) for _ in range(size)]
        #список случайных чисел для работы с сортировкой bucket
        float_data = [random.random() for _ in range(size)]

        int_sorts = [
            (bubble_sort, 'bubble', int_data),
            (quick_sort,'quick', int_data),
            (counting_sort,'counting', int_data),
            (radix_sort,'radix', int_data),
            (heap_sort,'heap', int_data),
            (sorted, "sort standarted", int_data),
        ]

        if size <=500:
            float_sorts=[(bucket_sort, "bucket", float_data)]
        else:
            float_sorts=[]
        print('')
        for func, name, data in int_sorts +float_sorts:
            try:
                time_f = benchmark_sort(func, data, name)
                print(f"{name}: {time_f} seconds")
            except Exception as e:
                print(f"{name}: {e}")

if __name__ == "__main__":
    compare_sorts()