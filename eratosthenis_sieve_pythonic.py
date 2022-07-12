# This function generates prime numbers up to a user specified maximum `N`.
# The algorithm used is the Sieve of Eratosthenes.
# It is quite simple. Given an array of integers from 1 to `N`, cross out all multiples
# of 2. Find the next uncrossed integer, and cross out all of its multiples.
# Repeat until you have passed the square root of `N`.
# The uncrossed numbers that remain are all the primes less than `N`.

# quick notice: this is a verbatic port of a Java code to Julia,
# and as such it is unreasonably low level.


def eratosthenis_sieve(N):
    prime = [True for i in range(N + 1)]  # boolean array
    p = 2
    while p * p <= N:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p
            for i in range(p * p, N + 1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, N + 1) if prime[p]]


print(eratosthenis_sieve(10))
