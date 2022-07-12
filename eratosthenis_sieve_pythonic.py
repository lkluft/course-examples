# This function generates prime numbers up to a user specified maximum `N`.
# The algorithm used is the Sieve of Eratosthenes.
# It is quite simple. Given an array of integers from 1 to `N`, cross out all multiples
# of 2. Find the next uncrossed integer, and cross out all of its multiples.
# Repeat until you have passed the square root of `N`.
# The uncrossed numbers that remain are all the primes less than `N`.


def eratosthenis_sieve(N):
    prime = [i > 1 for i in range(N + 1)]  # (initialize 0 and 1 to False)
    p = 0
    while p * p <= N:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p
            for i in range(p * p, N + 1, p):
                prime[i] = False
        p += 1

    return [i for i, p in enumerate(prime) if p]


print(eratosthenis_sieve(50))
