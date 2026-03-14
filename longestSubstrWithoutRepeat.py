from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = defaultdict(int)
        leftPointer = 0
        maxLength = 0

        for rightPointer in range(0, len(s)):
            hashMap[s[rightPointer]] += 1
            while hashMap[s[rightPointer]] > 1:
                hashMap[s[leftPointer]] -= 1
                leftPointer += 1
            maxLength = max(maxLength, rightPointer - leftPointer + 1)
        
        return maxLength

