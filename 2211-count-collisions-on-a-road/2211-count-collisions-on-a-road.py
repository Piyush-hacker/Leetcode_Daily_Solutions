class Solution(object):
    def countCollisions(self, directions):
        l = 0
        r = len(directions) - 1
        
        # 1. Skip cars moving left on the far left (they never collide)
        while l <= r and directions[l] == 'L':
            l += 1
            
        # 2. Skip cars moving right on the far right (they never collide)
        while r >= l and directions[r] == 'R':
            r -= 1
            
        count = 0
        # 3. Any moving car (L or R) remaining in the middle will collide
        for i in range(l, r + 1):
            if directions[i] != 'S':
                count += 1
                
        return count
        