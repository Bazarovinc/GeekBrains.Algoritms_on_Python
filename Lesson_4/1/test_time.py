"""Итак, в этом задании требовалось определаить сколько чисел в диапазоне от 2 до 99 кратны числам в диапазоне от 2 до 9
    Возьмем первый диапазон равный n, для анализа скорости алгоритма и его разновидностей."""

import timeit
import cProfile
import sys
"""В первой вариации алгоритма, мы просто проходимся по числам от 2 до и от 2 до 9, не создавая никаких массивов."""

sys.setrecursionlimit(10000)

def count_1(n):
    d = {}
    for i in range(2, 10):
        for j in range(2, n):
            if j % i == 0:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
    return d
# 10: 100 loops, best of 5: 13.2 usec per loop
# 100: 100 loops, best of 5: 60.3 usec per loop"""
# 200: 100 loops, best of 5: 120 usec per loop
# 500: 100 loops, best of 5: 312 usec per loop
# 1000: 100 loops, best of 5: 726 usec per loop
# 5000: 100 loops, best of 5: 3.73 msec per loop
# 10000: 100 loops, best of 5: 7.72 msec per loop
# 50000: 100 loops, best of 5: 45 msec per loop
# 10000: 100 loops, best of 5: 93.7 msec per loop
""" 
100:
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 test_time.py:9(count_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
100000:
4 function calls in 0.106 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.106    0.106 <string>:1(<module>)
        1    0.106    0.106    0.106    0.106 test_time.py:9(count_1)
        1    0.000    0.000    0.106    0.106 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""Во второй версии алгоритма, мы сначала создаем массивы, а потом делаем проходы по ним. Видел такую реализацию, когда
    проверял"""


def count_2(n):
    arr1 = [i for i in range(2, n)]
    arr2 = [i for i in range(2, 10)]
    d = {}
    for i in arr2:
        for j in arr1:
            if j % i == 0:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
    return d
# 10: 100 loops, best of 5: 6.48 usec per loop
# 100: 100 loops, best of 5: 61.3 usec per loop
# 200: 100 loops, best of 5: 122 usec per loop
# 500: 100 loops, best of 5: 306 usec per loop
# 1000: 100 loops, best of 5: 646 usec per loop
# 5000: 100 loops, best of 5: 3.3 msec per loop
# 10000: 100 loops, best of 5: 6.75 msec per loop
# 50000: 100 loops, best of 5: 41.4 msec per loop
# 100000: 100 loops, best of 5: 87.6 msec per loop
"""
100:
6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 test_time.py:56(count_2)
        1    0.000    0.000    0.000    0.000 test_time.py:57(<listcomp>)
        1    0.000    0.000    0.000    0.000 test_time.py:58(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
100000:
6 function calls in 0.098 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.098    0.098 <string>:1(<module>)
        1    0.094    0.094    0.097    0.097 test_time.py:56(count_2)
        1    0.003    0.003    0.003    0.003 test_time.py:57(<listcomp>)
        1    0.000    0.000    0.000    0.000 test_time.py:58(<listcomp>)
        1    0.000    0.000    0.098    0.098 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""Алгоритм с рекурсией"""


def count_n(n, i, count):
    if n == 2:
        if n % i == 0:
            return count + 1
        else:
            return count
    else:
        if n % i == 0:
            return count_n(n - 1, i, count + 1)
        else:
            return count_n(n - 1, i, count)


def count_3(n):
    d = {}
    for i in range(2, 10):
        d[i] = count_n(n - 1, i, 0)
    return d

# 10: 100 loops, best of 5: 12.6 usec per loop
# 100: 100 loops, best of 5: 155 usec per loop
# 200: 100 loops, best of 5: 122 usec per loop
# 500: 100 loops, best of 5: 823 usec per loop
# 1000: 100 loops, best of 5: 1.98 msec per loop
# 2000: 100 loops, best of 5: 4.38 msec per loop
# 3000: 100 loops, best of 5: 7.08 msec per loop
# 4000: 100 loops, best of 5: 9.84 msec per loop
# 5000: 100 loops, best of 5: 12.7 msec per loop
# 6000: 100 loops, best of 5: 16 msec per loop
# 7000: MemoryError: Stack overflow
"""
10:
68 function calls (12 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     64/8    0.000    0.000    0.000    0.000 test_time.py:108(count_n)
        1    0.000    0.000    0.000    0.000 test_time.py:121(count_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
100:
788 function calls (12 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    784/8    0.000    0.000    0.000    0.000 test_time.py:108(count_n)
        1    0.000    0.000    0.000    0.000 test_time.py:121(count_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
200:
1588 function calls (12 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
   1584/8    0.001    0.000    0.001    0.000 test_time.py:108(count_n)
        1    0.000    0.000    0.001    0.001 test_time.py:121(count_3)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
500:
3988 function calls (12 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
   3984/8    0.001    0.000    0.001    0.000 test_time.py:108(count_n)
        1    0.000    0.000    0.001    0.001 test_time.py:121(count_3)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
1000:
7988 function calls (12 primitive calls) in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
   7984/8    0.009    0.000    0.009    0.001 test_time.py:108(count_n)
        1    0.000    0.000    0.009    0.009 test_time.py:121(count_3)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
5000:
39988 function calls (12 primitive calls) in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
  39984/8    0.025    0.000    0.025    0.003 test_time.py:108(count_n)
        1    0.000    0.000    0.025    0.025 test_time.py:121(count_3)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
"""Итак, как видим, самый эффективный алгоритм-это второй, с созданием массива элементов и последующим обходом их.
    Лично я думал, что в данном случае, скорость будет n^2 + 8^2. Но как оказалось, скорость линейна."""