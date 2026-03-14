from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr not in hashMap:
                hashMap[sortedStr] = [s]
            else:
                hashMap[sortedStr].append(s)
        
        res = []
        for anagramList in hashMap.values():
            res.append(anagramList)
        
        return res
