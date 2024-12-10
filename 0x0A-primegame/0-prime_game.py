#!/usr/bin/python3
"""
Determines the winner of the game played by Maria and Ben.

:param x: The number of rounds.
:param nums: A list of n values, where each
value specifies the range of numbers for a round
:return: The name of the player who won
the most rounds, or None if it's a tie.
"""


def isWinner(x, nums):
    """
    Determines the winner of the game played by Maria and Ben.

    :param x: The number of rounds.
    :param nums: A list of n values, where each
    value specifies the range of numbers for a round
    :return: The name of the player who won
    the most rounds, or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    def sieve_primes(max_n):
        """Generates a list of cumulative counts of primes up to max_n."""
        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(max_n**0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, max_n + 1, i):
                    primes[multiple] = False

        prime_count = [0] * (max_n + 1)
        for i in range(1, max_n + 1):
            prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

        return prime_count

    max_n = max(nums)
    prime_count = sieve_primes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_used = prime_count[n]
        if primes_used % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
