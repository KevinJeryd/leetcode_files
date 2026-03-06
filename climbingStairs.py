# You are given an integer n representing the number of steps to reach he top of a staircase. You can climb with either 1 or 2 steps at a time.
#
# Return the number of distinct ways to climb to the top of the staircase.

class Solution:
    def climbStairs(self, n):
        cache = {}
        def recurse(n):
            if n == 0 or n == 1:
                return 1
            
            if n in cache:
                return cache[n]

            cache[n] = recurse(n-1) + recurse(n-2)

            return cache[n]

        return recurse(n)
        
