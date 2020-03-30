import timeit

def sieve(n):
    if n == 1:
        n = 2
    elif n == 0:
        return -1
    sieve = [i for i in range(n * n)]
    sieve[1] = 0
    prime_n = []
    for i in range(2, n * n):
        if sieve[i] != 0:
            j = i * 2
            prime_n.append(sieve[i])
            while j < n * n:
                sieve[j] = 0
                j += i
        if len(prime_n) == n:
            break

    return prime_n[n - 1]
