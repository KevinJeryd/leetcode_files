# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return num

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        l = 1
        r = n

        while l <= r:
            mid = l + (r - l) // 2

            if guess(mid) > 0:
                l = mid + 1
            elif guess(mid) < 0:
                r = mid - 1
            else:
                return mid

        return -1
