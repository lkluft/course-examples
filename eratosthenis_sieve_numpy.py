# This function generates prime numbers up to a user specified maximum `N`.
# The algorithm used is the Sieve of Eratosthenes.
# It is quite simple. Given an array of integers from 1 to `N`, cross out all multiples
# of 2. Find the next uncrossed integer, and cross out all of its multiples.
# Repeat until you have passed the square root of `N`.
# The uncrossed numbers that remain are all the primes less than `N`.
import numpy as np


def eratosthenis_sieve(N):
    is_prime = np.ones(N, dtype=bool)
    is_prime[:2] = False

    p = 0
    while p * p <= N:
        # If prime[p] is not changed, then it is a prime
        if is_prime[p]:
            is_prime[p*p:N+1:p] = False  # Updating all multiples of p
        p += 1

    return np.arange(N)[is_prime]


def test_primes():
    assert 0 not in eratosthenis_sieve(10), "0 is not a prime."
    assert 1 not in eratosthenis_sieve(10), "1 is not a prime."
    assert len(eratosthenis_sieve(10)) == 4, "There are four primes until 10."
    assert len(eratosthenis_sieve(100)) == 25, "There are 25 primes until 100."


if __name__ == "__main__":
    print(eratosthenis_sieve(10))
