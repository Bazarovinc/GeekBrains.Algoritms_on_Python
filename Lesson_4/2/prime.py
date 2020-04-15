import timeit

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def prime(n):
    if n == 1:
        n = 2
    elif n == 0:
        return -1
    prime_nums = []
    for i in range(2, n * n):
        if IsPrime(i):
            prime_nums.append(i)
        if len(prime_nums) == n:
            break
    return prime_nums[n - 1]
