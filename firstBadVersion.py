# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version is None

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n

        while l <= r:
            m = l + (r - l) // 2

            if isBadVersion(m): # If current version is bad, we know everything after it is bad, check earlier versions
                r = m - 1
            else:
                l = m + 1
            
        return l # The earliest bad version will have converged at l
