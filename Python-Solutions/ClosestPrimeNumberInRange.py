from typing import List
class Solution:
    # Time Limit Exceeded
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n == 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        primes = []
        for i in range(left, right + 1):
            if isPrime(i):
                primes.append(i)
        
        if not primes or len(primes) == 1:
            return [-1, -1]
        minRange = float('inf')
        leftIndex = 0
        rightIndex = 0
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < minRange:
                minRange = primes[i + 1] - primes[i]
                leftIndex = i
                rightIndex = i + 1
        return [primes[leftIndex], primes[rightIndex]]