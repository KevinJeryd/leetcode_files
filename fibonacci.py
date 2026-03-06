class Solution:
    def fibonacci(self, n, cache={}):
        if n in cache:
            return cache[n]       # already computed, skip the recursion entirely

        # Base cases
        if n == 0:
            return 0

        if n == 1:
            return 1

        # Compute actual fibonacci and put it in the cache
        cache[n] = Solution.fibonacci(self, n-1, cache) + Solution.fibonacci(self, n-2, cache)

        return cache[n]
