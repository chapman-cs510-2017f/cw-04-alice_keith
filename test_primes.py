#!/usr/bin/env python3

import primes

def test_primes():
    assert primes.eratosthenes(60) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    assert primes.eratosthenes(34) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]