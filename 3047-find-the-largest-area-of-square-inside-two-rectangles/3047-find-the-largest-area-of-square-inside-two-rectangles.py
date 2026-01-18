class Solution :
    def largestSquareArea( self, bottomLeft : List[List[int]], topRight : List[List[int]] ) -> int :
        rectangles = sorted([(x1, x2, y1, y2) for (x1, y1), (x2, y2) in zip(bottomLeft, topRight)], key = lambda x : x[0])
        maxSide = 0
        for index in range(len(rectangles)) :
            rect1 = rectangles[index]
            for jndex in range(index + 1, len(rectangles)) :
                rect2 = rectangles[jndex]
                if rect2[0] >= rect1[1] :
                    break
                width = min(rect1[1], rect2[1]) - max(rect1[0], rect2[0])
                height = min(rect1[3], rect2[3]) - max(rect1[2], rect2[2])
                if width > 0 and height > 0 :
                    maxSide = max(maxSide, min(width, height))
        return maxSide**2