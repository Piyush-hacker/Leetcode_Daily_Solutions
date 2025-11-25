class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1 
        
        index = 1
        length = 1
        while index % k != 0:
            index = (index * 10 + 1) % k
            length += 1
        return length

        