from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)

        rejected = 0
        sandwichCount = 0

        while rejected != len(queue):
            if queue[0] == sandwiches[sandwichCount]:
                queue.popleft()
                sandwichCount += 1
                rejected = 0
            else:
                val = queue.popleft()
                queue.append(val)
                rejected += 1
        
        return len(queue)
