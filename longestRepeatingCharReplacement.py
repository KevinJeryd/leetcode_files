class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        leftPos = 0
        mostFreqChar = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            mostFreqChar = max(mostFreqChar, count[s[r]])

            while (r - leftPos + 1) - mostFreqChar > k:
                count[s[leftPos]] -= 1
                leftPos += 1
            
            res = max(res, r - leftPos + 1)
        
        return res
